import test

def how_are(subj='world'):
    test.hello(subj)
    print 'How are you {}?'.format(subj)
    

if __name__ == '__main__':
    how_are()
    how_are('Leningrad')