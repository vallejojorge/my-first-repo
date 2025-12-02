import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Example function
def divide(a, b):
    logging.info('Dividing %s by %s', a, b)
    try:
        result = a / b
    except ZeroDivisionError:
        logging.error('Attempted to divide by zero')
        return None
    logging.debug('Result: %s', result)
    return result

# Call the function
divide(10, 2)
divide(10, 0)
