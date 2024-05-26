def display_hangman(tries): # hangman diagram
    stages = [
        r'''
           ------
           |    |
           |    O
           |   \|/
           |    |
           |   / \
           -
        ''', # sixth and final incorrect try
        r'''
           ------
           |    |
           |    O
           |   \|/
           |    |
           |   / 
           -
        ''', # fifth incorrect try
        r'''
           ------
           |    |
           |    O
           |   \|/
           |    |
           |    
           -
        ''', #fourth incorrect try
        r'''
           ------
           |    |
           |    O
           |   \|/
           |    
           |    
           -
        ''', #third incorrect try
        r'''
           ------
           |    |
           |    O
           |   \|
           |    
           |    
           - 
        ''',# second incorrect try
        '''
           ------
           |    |
           |    O
           |    |
           |    
           |    
           -  
        ''',# first incorrect try
        r'''
           ------
           |    |
           |    
           |    
           |    
           |    
           -
        ''' #initial figgure
    ]
    return stages[tries]
