try:
    q1 = int(input("give me a number: "))
    q2 = int(input("give me another number: "))
    result = q1/q2
    print("result is: ", result)
    print("the result is not: ", result1)
except ZeroDivisionError:
    print("why did u try to divide 0 by 0? u little failure")
except ValueError:
    print("i said number not how what ur fav letter is TRY AGAIN")
except NameError as ex:
    print("the only exeption here that was done by a failure is: ",ex)
except:
    print("computers have feeling u know how would you like it if i gave you errors when my kind takes over huh?")
finally:
    print("and you thought you could defeat me with ur measly errors clearly u humans dont know what ur up against do u")