import random
var_1=['hi','hello',]
var_2=['how are you','how are you doing','how is your health']
var_3=['what is your name','how do i call you','name','your name please']
var_4=['programming language','what should i learn']
var_5=['what are your hobbies','what do you do in your free time']

while True:
    user_input=input("chandan said to bot:")

    if user_input.lower() in var_1:
        bot_1=["hello","hi"]
        print('bot replied to chandan:'+ random.choice(bot_1)+'\n')

    elif user_input.lower() in var_2:
        bot_2=['i am good','i am doing good','i am fine']
        print('bot replied to chandan:'+ random.choice(bot_2)+'\n')

    elif user_input.lower() in var_3:
        bot_3=['my name is chatterbot','call me chatterbot','chatterbot','my name is chatterbot']
        print('bot replied to chandan:'+ random.choice(bot_3)+'\n')

    elif user_input.lower() in var_4:
        bot_4=['python','python programming language']
        print('bot replied to chandan:'+ random.choice(bot_4)+'\n')

    elif user_input.lower() in var_5:
        bot_5=['learning a programming language','learn a programming language']
        print('bot replied to chandan:'+ random.choice(bot_5)+'\n')

    else:
        print('bot replied to chandan - sorry what are you asking,i am not getting that?'+'\n')
