# if div by 3 then print fizz
# if div by 5 then print buzz
# if div by both then print fizzbuzz

def main(num:int) -> list:
    result = []
    for i in range(1, num + 1):
        if i%3 == 0 and i%5 == 0:
            result.append('fizzbuzz')
        elif i%3 == 0:
            result.append('fizz')
        elif i%5 == 0:
            result.append('buzz')
        else:
            result.append(i)
    return result