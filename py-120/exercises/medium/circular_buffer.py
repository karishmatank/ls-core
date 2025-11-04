# Version 1 - technically not circular, but much easier way to implement
class CircularBuffer:
    def __init__(self, buffer_size):
        self.buffer_size = buffer_size
        self._buffer = []
    
    @property
    def buffer_size(self):
        return self._buffer_size
    
    @buffer_size.setter
    def buffer_size(self, size):
        if not isinstance(size, int):
            raise TypeError("Size must be int")
        self._buffer_size = size
    
    def put(self, obj):
        self._buffer.append(obj)
        if len(self._buffer) > self.buffer_size:
            self.get()
    
    def get(self):
        if self._buffer:
            return self._buffer.pop(0)
        return None

    
    
buffer = CircularBuffer(3)

print(buffer.get() is None)          # True

buffer.put(1)
buffer.put(2)
print(buffer.get() == 1)             # True

buffer.put(3)
buffer.put(4)
print(buffer.get() == 2)             # True

buffer.put(5)
buffer.put(6)
buffer.put(7)
print(buffer.get() == 5)             # True
print(buffer.get() == 6)             # True
print(buffer.get() == 7)             # True
print(buffer.get() is None)          # True

buffer2 = CircularBuffer(4)

print(buffer2.get() is None)         # True

buffer2.put(1)
buffer2.put(2)
print(buffer2.get() == 1)            # True

buffer2.put(3)
buffer2.put(4)
print(buffer2.get() == 2)            # True

buffer2.put(5)
buffer2.put(6)
buffer2.put(7)
print(buffer2.get() == 4)            # True
print(buffer2.get() == 5)            # True
print(buffer2.get() == 6)            # True
print(buffer2.get() == 7)            # True
print(buffer2.get() is None)         # True



# Version 2 (more circular)
class CircularBuffer:
    def __init__(self, buffer_size):
        self._buffer_size = buffer_size
        self._buffer = [None] * self.buffer_size
        self._next_idx = 0
        self._oldest_idx = 0
    
    @property
    def buffer_size(self):
        return self._buffer_size
    
    def _is_buffer_full(self):
        return None not in self._buffer
        
    def put(self, obj):
        self._buffer[self._next_idx] = obj
        self._next_idx = (self._next_idx + 1) % self.buffer_size
        if self._is_buffer_full():
            self._oldest_idx = self._next_idx
    
    def get(self):
        oldest = self._buffer[self._oldest_idx]
        if oldest is not None:
            self._buffer[self._oldest_idx] = None
            self._oldest_idx = (self._oldest_idx + 1) % self.buffer_size
        return oldest

    
    
buffer = CircularBuffer(3)

print(buffer.get() is None)          # True

buffer.put(1)
buffer.put(2)
print(buffer.get() == 1)             # True

buffer.put(3)
buffer.put(4)
print(buffer.get() == 2)             # True

buffer.put(5)
buffer.put(6)
buffer.put(7)
print(buffer.get() == 5)             # True
print(buffer.get() == 6)             # True
print(buffer.get() == 7)             # True
print(buffer.get() is None)          # True

buffer2 = CircularBuffer(4)

print(buffer2.get() is None)         # True

buffer2.put(1)
buffer2.put(2)
print(buffer2.get() == 1)            # True

buffer2.put(3)
buffer2.put(4)
print(buffer2.get() == 2)            # True

buffer2.put(5)
buffer2.put(6)
buffer2.put(7)
print(buffer2.get() == 4)            # True
print(buffer2.get() == 5)            # True
print(buffer2.get() == 6)            # True
print(buffer2.get() == 7)            # True
print(buffer2.get() is None)         # True