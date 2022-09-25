# Exception handling
# Exception and error
# The problem which can be handled by the program is called exception
# The problem which can not be handled by program is called error


# try and except block

# try:
#     x = 5
#     y = 1
#     result = x / 1
#     print(result)
#     name  = 'None'
#     name.upper()
#     l1=[1]
#     print(l1[0])
#
#
# except ZeroDivisionError as ex:
#     print("Don't pass zero value")
#
# except AttributeError as ex:
#     print("Value should not be null")
#
# except IndexError as ex:
#     print("Index should be lesser than length")
#
# except Exception as ex:
#     print(ex)
#
# # finally:
# #     print("I am in finally block")
# else:
#     print("else block")
#
# print('I am executing next program')
#
# for i in range(3):
#     if i == 2:
#         break
#     print(i)
# else:
#     print("I am in for else block")


def sample():
    try:
        x = 5
        y = 1
        result = x / 0
        return  True
    except:
        return False

    finally:
        return "finally block from sample function"

    # else:
    #    print("else")


value = sample()
print(value)