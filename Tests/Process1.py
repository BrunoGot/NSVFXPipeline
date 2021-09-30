"""Testing multiprocess data transmission between two scripts"""

from multiprocessing import Process, Pipe

def f(child_conn): #child_conn = le pipe
    msg = "Hello"
    child_conn.send(msg)
    child_conn.close()