def main():

    speed = int(input('What is the speed of the vehicle in MPH? '))
    time = int(input('How many hours has it traveled? '))
    hour = 0
    
    
    print('Hour   ''Distance Traveled')
    print('------------------------')

    while hour < time:
        hour += 1
        distance = speed * hour
        ##speed += speed
        print(hour,'\t',distance)
        
main()

    
    
