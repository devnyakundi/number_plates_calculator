#Author: George Nyaribo
#Source of Kenyan Number plate system information https://en.wikipedia.org/wiki/Vehicle_registration_plates_of_Kenya

import string
import re


# Solution
# 1. Check the format of the start and finish.
#   - if Invalid stop and return an error 
#   - iF all is well, start the number calculations
# - Confirm from the wikipedia the number plate sequences that were not used at all
#. -

#


number_plate_format_7 = re.compile("^[K][ABC][A-Z][0-9]{3}[A-Z]$")
number_plate_format_6 = re.compile("^[K][ABC][A-Z][0-9]{3}$")
#These number plates shouldn't be created
omitted_plates = ['KAF', 'KAO', 'KAI', 'KBI', 'KBO', 'KCO', 'KCI']
plates_produced = []
errors_ = []


def numberOfCars(start, finish):
    if start and finish:
        # convert to uppercase and remove all spaces
        first = start.upper().replace(" ", "")
        last = finish.upper().replace(" ", "")
        if(len(first) == 6 and len(last) == 6):
            if number_plate_format_6.match(first) and number_plate_format_6.match(last):
                print('Correct Number plate format')
                if(last > first):
                    print('Not Implemented Yet')
                else:
                    print(
                        'The last Number place is earlier than the first one, please update your inputs')
            else:
                print('Bad number plate format')
        elif(len(first) == 7 and len(last) == 7):
            if number_plate_format_7.match(first) and number_plate_format_7.match(last):
                print('Correct number plate format')
                if(last >= first):
                    print('Now Calculating the number of Cars between ',
                          first, ' and ', last)
                    if((first[0:3] in omitted_plates) or (last[0:3] in omitted_plates)):
                        print(
                            'Sorry: One of the provided plate numbers was never produced')
                    else:
                        first_split = list(first)
                        last_split = list(last)
                        # we'll check and compare where the provided number plates differ so as to know where to start our calculations
                        # The approach i took was to start from the outermost position then work inwards. 
                        # But since the first Item in the Civilian Number plate doesn't change i thought it wise to start from the second position
                        # lists are zero indexed 
                        if(first_split[1] == last_split[1]):
                            if(first_split[2] == last_split[2]):
                                if(first_split[3] == last_split[3]):
                                    if(first_split[4] == last_split[4]):
                                        if(first_split[5] == last_split[5]):
                                            if(first_split[6] == last_split[6]):
                                                #no difference found which means the number plate provided was the same , hence return that one number plate
                                               insert_number_plate(first)
                                            else:
                                                
                                                for item in range(ord(first_split[6]), ord(last_split[6])+1, 1):
                                                    #this eliminates the O and I from the Number plates. TODO: use a function instead
                                                    if (chr(item) == 'O' or chr(item) == 'I'):
                                                        pass
                                                    else:
                                                        insert_number_plate(first[:-1] + chr(item))
                                        else:
                                            start_range = range(int(first_split[5]), int(last_split[5]) + 1, 1)
                                            # loop over the items so as to treat the first and last items separately from all the others. 
                                            # I have done this in most parts of the code below.
                                            start_range_iter = enumerate(start_range)
                                            for c, item_2 in start_range_iter:
                                                if c == 0:
                                                    for item_3 in range(ord(first_split[6]), ord('Z') + 1, 1):
                                                        if (chr(item_3) == 'O' or chr(item_3) == 'I'):
                                                            pass
                                                        else:
                                                            insert_number_plate(first[:-2] + str(item_2) + chr(item_3))
                                                elif c == len(start_range) - 1:
                                                    for item_4 in range(ord('A'), ord(last_split[6]) + 1, 1):
                                                        if (chr(item_4) == 'O' or chr(item_4) == 'I'):
                                                            pass
                                                        else:
                                                            insert_number_plate(
                                                                first[:-2] + str(item_2) + chr(item_4))
                                                else:
                                                    for item_5 in range(ord('A'), ord('Z') + 1, 1):
                                                        if (chr(item_5) == 'O' or chr(item_5) == 'I'):
                                                            pass
                                                        else:
                                                            insert_number_plate(
                                                                first[:-2] + str(item_2) + chr(item_5)) 

                                            # for item_2 in range(int(first_split[5]), int(last_split[5]) + 1, 1):
                                            #     if item_2 == int(first_split[5]):
                                            #         for item_3 in range(ord(first_split[6]), ord('Z') + 1, 1):
                                            #             if (chr(item_3) == 'O' or chr(item_3) == 'I'):
                                            #                 pass
                                            #             else:
                                            #                 insert_number_plate(first[:-2] + str(item_2) + chr(item_3))
                                            #     elif item_2 == int(last_split[5]):
                                            #         for item_4 in range(ord('A'), ord(last_split[6]) + 1, 1):
                                            #             if (chr(item_4) == 'O' or chr(item_4) == 'I'):
                                            #                 pass
                                            #             else:
                                            #                 insert_number_plate(
                                            #                     first[:-2] + str(item_2) + chr(item_4))
                                            #     else:
                                            #         for item_5 in range(ord('A'), ord('Z') + 1, 1):
                                            #             if (chr(item_5) == 'O' or chr(item_5) == 'I'):
                                            #                 pass
                                            #             else:
                                            #                 insert_number_plate(
                                            #                     first[:-2] + str(item_2) + chr(item_5))
                                    else:
                                        print(
                                            '4 - Start generating the values from', first)
                                        outer_range = range(
                                            int(first_split[4]), int(last_split[4]) + 1, 1)
                                        outer_range_iter = enumerate(
                                            outer_range)
                                        for i, item_6 in outer_range_iter:
                                            inner_range = range(
                                                int(first_split[5]), 10, 1)
                                            inner_range_iter = enumerate(
                                                inner_range)
                                            if i == 0:
                                                for j, item_7 in inner_range_iter:
                                                    if j == 0:
                                                        inner_range_1 = range(
                                                            ord(first_split[6]), ord('Z') + 1, 1)
                                                    else:
                                                        inner_range_1 = range(
                                                            ord('A'), ord('Z') + 1, 1)
                                                    for item_10 in inner_range_1:
                                                        if (chr(item_10) == 'O' or chr(item_10) == 'I'):
                                                            pass
                                                        else:
                                                            insert_number_plate(
                                                                first[:-3] + str(item_6) + str(item_7) + chr(item_10))
                                            elif i == len(outer_range) - 1:
                                                inner_range = range(
                                                    0, int(last_split[5])+1, 1)
                                                inner_range_iter = enumerate(
                                                    inner_range)
                                                for k, item_8 in inner_range_iter:
                                                    if k == len(inner_range) - 1:
                                                        inner_range_2 = range(
                                                            ord('A'), ord(last_split[6]) + 1, 1)
                                                    else:
                                                        inner_range_2 = range(
                                                            ord('A'), ord('Z') + 1, 1)

                                                    for item_11 in inner_range_2:
                                                        if (chr(item_11) == 'O' or chr(item_11) == 'I'):
                                                            pass
                                                        else:
                                                            insert_number_plate(
                                                                first[:-3] + str(item_6) + str(item_8) + chr(item_11))
                                            else:
                                                inner_range = range(0, 10, 1)
                                                for item_9 in inner_range:
                                                    for item_12 in range(ord('A'), ord('Z') + 1, 1):
                                                        if (chr(item_12) == 'O' or chr(item_12) == 'I'):
                                                            pass
                                                        else:
                                                            insert_number_plate(
                                                                first[:-3] + str(item_6) + str(item_9) + chr(item_12))

                                else:
                                    print(
                                        '3 - Start generating the values from', first)
                                    ex_outer_range = range(
                                        int(first_split[3]), int(last_split[3]) + 1, 1)
                                    ex_outer_range_iter = enumerate(
                                        ex_outer_range)
                                    for l, item_13 in ex_outer_range_iter:
                                        ex_inner_range = range(
                                            int(first_split[4]), 10, 1)
                                        ex_inner_range_iter = enumerate(
                                            ex_inner_range)
                                        if l == 0:
                                            for j, item_18 in ex_inner_range_iter:
                                                if j == 0:
                                                    ex_inner_range_1 = range(
                                                        int(first_split[5]), 10, 1)
                                                else:
                                                    ex_inner_range_1 = range(
                                                        0, 10, 1)

                                                ex_inner_range_1_iter = enumerate(
                                                    ex_inner_range_1)

                                                for m, item_19 in ex_inner_range_1_iter:
                                                    if m == 0 and j == 0:
                                                        ex_inner_range_1_1 = range(
                                                            ord(first_split[6]), ord('Z')+1, 1)
                                                    else:
                                                        ex_inner_range_1_1 = range(
                                                            ord('A'), ord('Z')+1, 1)

                                                    for item_20 in ex_inner_range_1_1:
                                                        if (chr(item_20) == 'O' or chr(item_20) == 'I'):
                                                            pass
                                                        else:
                                                            insert_number_plate(
                                                                first[:-4] + str(item_13) + str(item_18) + str(item_19) + chr(item_20))
                                        elif l == len(ex_outer_range)-1:
                                            ex_inner_range = range(
                                                0, int(last_split[4])+1, 1)
                                            ex_inner_range_iter = enumerate(
                                                ex_inner_range)
                                            for n, item_21 in ex_inner_range_iter:
                                                if n == 0:
                                                    ex_inner_range_1 = range(
                                                        0, int(last_split[5])+1, 1)
                                                else:
                                                    ex_inner_range_1 = range(
                                                        0, 10, 1)

                                                ex_inner_range_1_iter = enumerate(
                                                    ex_inner_range_1)
                                                for p, item_22 in ex_inner_range_1_iter:
                                                    if p == len(ex_inner_range_1) - 1:
                                                        ex_inner_range_1_1 = range(
                                                            ord('A'), ord(last_split[6])+1, 1)
                                                    else:
                                                        ex_inner_range_1_1 = range(
                                                            ord('A'), ord('Z')+1, 1)

                                                    for item_23 in ex_inner_range_1_1:
                                                        if (chr(item_23) == 'O' or chr(item_23) == 'I'):
                                                            pass
                                                        else:
                                                            insert_number_plate(
                                                                first[:-4] + str(item_13) + str(item_21) + str(item_22) + chr(item_23))

                                        else:
                                            ex_inner_range = range(
                                                int(0), 10, 1)
                                            for item_15 in ex_inner_range:
                                                ex_inner_range_3 = range(
                                                    int(0), 10, 1)
                                                for item_16 in ex_inner_range_3:
                                                    ex_inner_range_3_1 = range(
                                                        ord('A'), ord('Z') + 1, 1)
                                                    for item_17 in ex_inner_range_3_1:
                                                        if (chr(item_17) == 'O' or chr(item_17) == 'I'):
                                                            pass
                                                        else:
                                                            insert_number_plate(
                                                                first[:-4] + str(item_15) + str(item_15) + str(item_16) + chr(item_17))

                            else:
                                print('2 - Start generating the values from', first)
                                int_outer_range = range(
                                    ord(first_split[2]), ord(last_split[2])+1, 1)
                                int_outer_ranger_iter = enumerate(
                                    int_outer_range)
                                for b, term_1 in int_outer_ranger_iter:
                                    if b == 0:
                                        int_outer_range_1 = range(
                                            int(first_split[3]), 10, 1)
                                        int_outer_range_1_iter = enumerate(
                                            int_outer_range_1)
                                        for c, term_1_1 in int_outer_range_1_iter:
                                            int_outer_range_1_1 = range(
                                                int(first_split[4]), 10, 1)
                                            if c == 0:
                                                int_outer_range_1_1 = range(
                                                    int(first_split[4]), 10, 1)
                                            else:
                                                int_outer_range_1_1 = range(
                                                    0, 10, 1)

                                            int_outer_range_1_1_iter = enumerate(
                                                int_outer_range_1_1)
                                            for d, term_1_1_1 in int_outer_range_1_1_iter:
                                                int_outer_range_1_1_1 = range(
                                                    int(first_split[5]), 10, 1)
                                                if d == 0:
                                                    int_outer_range_1_1_1 = range(
                                                        int(first_split[5]), 10, 1)
                                                else:
                                                    int_outer_range_1_1_1 = range(
                                                        0, 10, 1)
                                                int_outer_ranger_1_1_1_iter = enumerate(
                                                    int_outer_range_1_1_1)
                                                for f, term_1_1_1_1 in int_outer_ranger_1_1_1_iter:
                                                    int_outer_range_1_1_1_1 = range(
                                                        ord(first_split[6]), ord('Z') + 1, 1)
                                                    if f == 0:
                                                        int_outer_range_1_1_1_1 = range(
                                                            ord(first_split[6]), ord('Z') + 1, 1)
                                                    else:
                                                        int_outer_range_1_1_1_1 = range(
                                                            ord('A'), ord('Z') + 1, 1)

                                                    for term_1_1_1_1_1 in int_outer_range_1_1_1_1:
                                                        if (chr(term_1_1_1_1_1) == 'O' or chr(term_1_1_1_1_1) == 'I'):
                                                            pass
                                                        else:
                                                            insert_number_plate(first[:-5] + chr(term_1) + str(term_1_1) + str(
                                                                term_1_1_1) + str(term_1_1_1_1) + chr(term_1_1_1_1_1))

                                    elif b == len(int_outer_range) - 1:
                                        ext_outer_range_1 = range(
                                            0, int(last_split[3])+1, 1)
                                        ext_outer_ranger_1_iter = enumerate(
                                            ext_outer_range_1)
                                        for g, term_3 in ext_outer_ranger_1_iter:
                                            if g == len(ext_outer_range_1) - 1:
                                                ext_outer_range_1_1 = range(
                                                    0, int(last_split[4])+1, 1)
                                            else:
                                                ext_outer_range_1_1 = range(
                                                    0, 10, 1)

                                            ext_outer_range_1_1_iter = enumerate(
                                                ext_outer_range_1_1)
                                            for h, term_3_1 in ext_outer_range_1_1_iter:
                                                if h == len(ext_outer_range_1_1) - 1:
                                                    ext_outer_range_1_1_1 = range(
                                                        0, int(last_split[5])+1, 1)
                                                else:
                                                    ext_outer_range_1_1_1 = range(
                                                        0, 10, 1)

                                                ext_outer_range_1_1_1_iter = enumerate(
                                                    ext_outer_range_1_1_1)

                                                for q, term_3_1_1 in ext_outer_range_1_1_1_iter:
                                                    if q == len(ext_outer_range_1_1_1) - 1:
                                                        ext_outer_range_1_1_1_1 = range(
                                                            ord('A'), ord(last_split[6])+1, 1)
                                                    else:
                                                        ext_outer_range_1_1_1_1 = range(
                                                            ord('A'), ord('Z'), 1)

                                                    for term_3_1_1_1 in ext_outer_range_1_1_1_1:
                                                        if(term_3 == 0 and term_3_1 == 0 and term_3_1_1 == 0):
                                                            pass
                                                        else:
                                                            if (chr(term_3_1_1_1) == 'O' or chr(term_3_1_1_1) == 'I'):
                                                                pass
                                                            else:
                                                                insert_number_plate(
                                                                    first[:-5] + chr(term_1) + str(term_3) + str(term_3_1) + str(term_3_1_1) + chr(term_3_1_1_1))

                                               
                                    else:
                                        for term_2 in range(0, 10, 1):
                                            for term_2_1 in range(0, 10, 1):
                                                for term_2_1_1 in range(0, 10, 1):
                                                    if(term_2 == 0 and term_2_1 == 0 and term_2_1_1 == 0):
                                                        pass
                                                    else:
                                                        for term_2_1_1_1 in range(ord('A'), ord('Z')+1, 1):
                                                            if (chr(term_2_1_1_1) == 'O' or chr(term_2_1_1_1) == 'I'):
                                                                pass
                                                            else:
                                                                insert_number_plate(
                                                                    first[:-5] + chr(term_1) + str(term_2) + str(term_2_1) + str(term_2_1_1) + chr(term_2_1_1_1))
                                                               

                        else:
                            print('1 - Start generating the values from', first)
                            final_outer_range = range(ord(first_split[1]), ord(last_split[1])+1, 1)
                            final_outer_ranger_iter = enumerate(final_outer_range)
                            for p, trm_1 in final_outer_ranger_iter:
                                if p == 0:
                                    final_outer_range_1 = range(ord(first_split[2]),ord('Z')+1,1)
                                    
                                    final_outer_ranger_1_iter = enumerate(final_outer_range_1)
                                    for q , trm_1_1 in final_outer_ranger_1_iter:
                                        if q == 0:
                                            final_outer_range_1_1 = range(int(first_split[3]),10,1)
                                        else:
                                            final_outer_range_1_1 = range(0,10,1)

                                        final_outer_range_1_1_iter = enumerate(final_outer_range_1_1)
                                        for r, trm_1_1_1 in final_outer_range_1_1_iter:
                                            if r == 0:
                                                final_outer_range_1_1_1 = range(int(first_split[4]),10,1)
                                            else:
                                                final_outer_range_1_1_1 = range(0,10,1)
                                            
                                            final_outer_range_1_1_1_iter = enumerate(final_outer_range_1_1_1)
                                            for s, trm_1_1_1_1 in final_outer_range_1_1_1_iter:
                                                if s == 0:
                                                    final_outer_range_1_1_1_1 = range(int(first_split[5]),10,1)
                                                else:
                                                    final_outer_range_1_1_1_1 = range(0,10,1)
                                                
                                                final_outer_range_1_1_1_1_iter = enumerate(final_outer_range_1_1_1_1)
                                                for t, trm_1_1_1_1_1 in final_outer_range_1_1_1_1_iter:
                                                    if t == 0:
                                                        final_outer_range_1_1_1_1_1 = range(ord(first_split[6]), ord('Z')+1, 1)
                                                    else:
                                                        final_outer_range_1_1_1_1_1 = range(ord('A'),ord('Z')+1,1)
                                                    for trm_1_1_1_1_1_1 in final_outer_range_1_1_1_1_1:
                                                        if(trm_1_1_1 == 0 and trm_1_1_1_1 == 0 and trm_1_1_1_1_1 == 0):
                                                            pass
                                                        else:
                                                            if (chr(trm_1_1_1_1_1_1) == 'O' or chr(trm_1_1_1_1_1_1) == 'I'):
                                                                pass
                                                            else:
                                                                 insert_number_plate(first[:-6] + chr(trm_1)+chr(trm_1_1) + str(trm_1_1_1) + str(trm_1_1_1_1)+str(trm_1_1_1_1_1) + chr(trm_1_1_1_1_1_1))
                                                                # pass
                                                       
                                elif p == len(final_outer_range) - 1:
                                    
                                    final_outer_range_2 = range(ord('A'),ord(first_split[2])+1,1)
                                    final_outer_range_2_iter = enumerate(final_outer_range_2)
                                    for g, tm_1 in final_outer_range_2_iter:
                                        if g == len(final_outer_range_2) - 1:
                                            final_outer_range_2_1 = range(0,int(last_split[3])+1,1)
                                        else:
                                            final_outer_range_2_1 = range(0,10,1)
                                        
                                        final_outer_range_2_1_iter = enumerate(final_outer_range_2_1)

                                        for h, tm_1_1 in final_outer_range_2_1_iter:
                                            if h == len(final_outer_range_2_1) - 1:
                                                final_outer_range_2_1_1 = range(0,int(last_split[4])+1,1)
                                            else:
                                                final_outer_range_2_1_1 = range(0,10,1)
                                            
                                            final_outer_range_2_1_1_iter = enumerate(final_outer_range_2_1_1)

                                            for r, tm_1_1_1 in final_outer_range_2_1_1_iter:
                                                if r ==len(final_outer_range_2_1_1) - 1:
                                                    final_outer_range_2_1_1_1 = range(0,int(last_split[5])+1,1)
                                                else:
                                                    final_outer_range_2_1_1_1 = range(0,10,1)
                                                final_outer_range_2_1_1_1_iter = enumerate(final_outer_range_2_1_1_1)
                                                for q, tm_1_1_1_1 in final_outer_range_2_1_1_1_iter:
                                                    if q == len(final_outer_range_2_1_1_1) - 1:
                                                        final_outer_range_2_1_1_1_1 = range(ord('A'),ord(last_split[6])+1,1)
                                                    else:
                                                        final_outer_range_2_1_1_1_1 = range(ord('A'),ord('Z')+1, 1)
                                                    
                                                    for tm_1_1_1_1_1 in final_outer_range_2_1_1_1_1:
                                                        if( tm_1_1 == 0 and tm_1_1_1 == 0 and tm_1_1_1_1 == 0):
                                                            pass
                                                        else:
                                                            if (chr(tm_1_1_1_1_1) == 'O' or chr(tm_1_1_1_1_1) == 'I'):
                                                                pass
                                                            else:
                                                                insert_number_plate(first[:-6]+chr(trm_1) + chr(tm_1) + str(tm_1_1) + str(tm_1_1_1) + str(tm_1_1_1_1) + chr(tm_1_1_1_1_1))

                                                
                                        
                                else:
                                    for trm_3 in range(ord('A'), ord('Z')+1,1):
                                        for trm_3_1 in range(0,10,1):
                                            for trm_3_1_1 in range(0,10,1):
                                                for trm_3_1_1_1 in range(0,10,1):
                                                    for trm_3_1_1_1_1 in range(ord('A'), ord('Z')+1,1):
                                                        if( trm_3_1 == 0 and trm_3_1_1 == 0 and trm_3_1_1_1 == 0):
                                                            pass
                                                        else:
                                                            if (chr(trm_3_1_1_1_1) == 'O' or chr(trm_3_1_1_1_1) == 'I'):
                                                                pass
                                                            else:
                                                                insert_number_plate(first[:-6] + chr(trm_1) + chr(trm_3) +str(trm_3_1) + str(trm_3_1_1) + str(trm_3_1_1_1) + chr(trm_3_1_1_1_1))
                                                                # pass


                else:
                    print(
                        'The last Number plate is earlier than the first number plate, please update your inputs')

            else:
                print('Bad number plate format')
        elif((len(first) == 7 and len(last) == 6) or (len(first) == 6 and len(last) == 7)):
            print('Un equal lengths')
        else:
            print('last')
    else:
        print('Please enter the requires arguments')
    # print(plates_produced)
    print('\n')
    print(len(plates_produced), 'Cars were produced')


def insert_number_plate(plate):
    if plate:
        # insert only valid number plates.
        if len(plate) == 7 and (plate[0:3] not in omitted_plates) and number_plate_format_7.match(plate):
            plates_produced.append(plate[0:3]+' '+plate[3::])


# numberOfCars('KAA 001S', 'KCA 232P')
numberOfCars('KAA 001s','KAA 004Q')


#To list the number plates
# Un comment line 486 print(plates_produced) and execute this file with > output.txt
