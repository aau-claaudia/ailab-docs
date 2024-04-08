import tensorflow as tf
import time

def benchmark_tensorflow():
    # Create some random data
    input_data = tf.random.normal((10000, 10000))

    # Define a simple TensorFlow computation (for example, matrix multiplication)
    @tf.function
    def some_computation(x):
        return tf.matmul(x, x)

    # Warm-up to ensure graph optimizations are done
    _ = some_computation(input_data)

    # Run the computation and measure the time
    start_time = time.time()
    result = some_computation(input_data)
    end_time = time.time()

    # Print the elapsed time
    print("Time taken: {:.4f} seconds".format(end_time - start_time))

if __name__ == "__main__":
    benchmark_tensorflow()