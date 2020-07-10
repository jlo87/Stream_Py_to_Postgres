# Ingest data from a mock API using a generator.
  
from flask import Flask, Response, stream_with_context
import time
import uuid
import random

APP = Flask(__name__)

# Create the mock endpoint. rowcount to test returned data:
@APP.route("/very_large_request/<int:rowcount>", methods=["GET"])
def get_large_request(rowcount):
    """returns N rows of data"""
    def f():
        """The generator of mock data"""
        for _i in range(rowcount):
            time.sleep(.01) # API speeds vary for real-life simulation.
            txid = uuid.uuid4()
            print(txid)
            uid = uuid.uuid4()
            amount = round(random.uniform(-1000, 1000), 2)
            yield f"('{txid}', '{uid}', {amount})\n"
    return Response(stream_with_context(f()))

if __name__ == "__main__":
    APP.run(debug=True)