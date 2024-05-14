Checkpointing is a technique used to ensure that your computational jobs can be resumed from a previously saved state in case of interruptions or failures. This guide outlines how to implement and use checkpointing effectively within your jobs using different applications.


TensorFlow:

TensorFlow provides native support for checkpointing during model training. Refer to the TensorFlow documentation for implementation details.
Keras:

If you're using the Keras interface, it also offers checkpointing mechanisms to save model states. Consult the Keras documentation for guidance.
PyTorch:

PyTorch includes support for checkpointing during model training. Check the PyTorch documentation for instructions on implementing checkpointing in your PyTorch-based applications.
1. Integration with Slurm and Singularity
When running jobs on a Slurm-managed HPC cluster with Singularity containers, ensure the following:

Include checkpointing logic within your job script or application.
Set up Slurm job scripts to handle checkpoint files appropriately.
If using Singularity containers, ensure that the checkpoint files are accessible within the container environment and are saved to a persistent location outside the container.
5. Best Practices
Determine optimal checkpoint intervals based on the nature of your workload and the potential impact of data loss.
Regularly test checkpointing functionality to ensure reliability and effectiveness.
Document checkpointing procedures for future reference and troubleshooting.
Conclusion
Implementing checkpointing in your HPC jobs using Slurm and Singularity is essential for minimizing data loss and maximizing computational efficiency. By following the guidelines outlined in this user guide and leveraging built-in checkpointing features of relevant libraries, you can enhance the robustness and resilience of your computational workflows.

For specific implementation details or troubleshooting assistance, refer to the documentation of the respective libraries and HPC management tools.


### TensorFlow checkpointing

TensorFlow provides native support for checkpointing during model training. Lets

!!! example
    ``` py linenums="1" hl_lines="34 35 36 37 38 39 40 41 42 43 48 49 50 51 52 58 59 60 61 62 63 66 67"
        import os
        import sys
        import os.path
        import tensorflow as tf
        from tensorflow import keras

        #####Get an example dataset - we'll use the MNIST dataset first 1000 examples:
        (train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()

        train_labels = train_labels[:5000]
        test_labels = test_labels[:5000]

        train_images = train_images[:5000].reshape(-1, 28 * 28) / 255.0
        test_images = test_images[:5000].reshape(-1, 28 * 28) / 255.0

        ##epoch number of steps for each job, get it as a commandline argument:
        epoch_steps=20

        ####Define a simple sequential model:
        def create_model():
        model = tf.keras.models.Sequential([
            keras.layers.Dense(512, activation='relu', input_shape=(784,)),
            keras.layers.Dropout(0.2),
            keras.layers.Dense(10)
        ])

        model.compile(optimizer='adam',
                        loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True),
                        metrics=[tf.metrics.SparseCategoricalAccuracy()])

        return model


        # Include the epoch in the file name (uses `str.format`)
        checkpoint_path = "checkpoints/{epoch:d}.ckpt"
        checkpoint_dir = os.path.dirname(checkpoint_path)

        # Create a callback that saves the model's weights every epoch (period=1)
        cp_callback = tf.keras.callbacks.ModelCheckpoint(
            filepath=checkpoint_path, 
            verbose=1, 
            save_weights_only=True,
            period=1)

        # Create a new model instance
        model = create_model()

        if os.path.exists(checkpoint_dir):
            # If there are existing checkpoints, load the latest one
            latest = tf.train.latest_checkpoint(checkpoint_dir)
            # Load the previously saved weights, if there are any:
            model.load_weights(latest)

            # Re-evaluate the model
            loss, acc = model.evaluate(test_images,  test_labels, verbose=2)
            print("Restored model, accuracy: {:5.2f}%".format(100*acc))

            # Get the step number from the latest checkpoint
            ckpt = tf.train.get_checkpoint_state(checkpoint_dir) 
            step = int(os.path.basename(ckpt.model_checkpoint_path).split('.')[0])
            print('Continuing calculation from epoch step:' + str(step)) 
            initialEpoch=step
        else:
            initialEpoch=0
            # Save the weights for the initial epoch
            model.save_weights(checkpoint_path.format(epoch=0))

        # Train the model with the new callback
        model.fit(train_images, 
                train_labels,
                epochs=epoch_steps, 
                initial_epoch=initialEpoch,
                callbacks=[cp_callback],
                validation_data=(test_images,test_labels),
                verbose=1)
    ```


### PyTorch