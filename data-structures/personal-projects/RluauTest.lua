Node = {value = nil, _next = nil}

function Node:setValue(self, val)
    self.value = val
end

Queue = {head = nil, tail = nil}

function Queue:push(self, val)
    if self.head == nil then
        local pointingnode = Node.setValue(val)
        self.head = pointingnode
        self.tail = pointingnode
    else
        local pointingnode = Node.setValue(val)
        local shovednode = self.head
        pointingnode._next = shovednode
        self.head = pointingnode
    end
end
