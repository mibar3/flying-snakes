def movingQueue():
  queue = []
  while len(queue) >= 0:
    print('If there is a new person in the queue add the name or \nif the queue can move along write next')
    input_list = input()
    if input_list != 'next':
      queue.append(input_list)
      print('you are on Position:', len(queue))
    else:
        if len(queue) > 0:
          print(queue[0],'can leave the queue')
          queue.pop(0)
        else:
          print('the queue is empty')
          break

movingQueue()
