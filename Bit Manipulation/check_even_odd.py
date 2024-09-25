x = ""
#do & with 1

i = 2
#000101
#&000100 <= 1<<i (left shift i)
# = 000100 > 0 => 1
        #    == 0 => 0
        
        
# def get_ith_bit(n,i):
#     mask = 1<<i
#     return(n&mask)>0 ? 1 : 0

# get_ith_bit(5)



def get_dtmf_extensions(events):
    dtmf_extensions = ''
    try:
        for num in range(1, 11):
            if events.get('dtmf_' + str(num)):
                dtmf_extensions += events.get('dtmf_' + str(num)) + ','
        dtmf_extensions = dtmf_extensions.strip(",")
    except:
        print("test")
        dtmf_extensions = ''
    return dtmf_extensions
    

events = {"dtmf_2": "1", 
            "dtmf_1": None}
print(get_dtmf_extensions(events))