import os
import json
import math

def json_splitter(file_name:str, max_file_size:int, del_original:bool=False):
    try:
        # request file name
        f = open(file_name)
        file_size = os.path.getsize(file_name)
        data = json.load(f)
        f.close()
        
        if isinstance(data, list):
            data_len = len(data)
            print('Valid JSON file found')

            if del_original == True:
                os.remove(file_name)
        else:
            print("JSON is not an Array of Objects")
            exit()
    except:
        print('Error loading JSON file ... exiting')
        exit()

    # get numeric input
    try:
        size_per_file = abs(float(max_file_size))
    except:
        print('Error entering maximum file size ... exiting')
        exit()

    # check that file is larger than max size
    if file_size < size_per_file:
        print('File smaller than split size, exiting')
        exit()

    # determine nukber of files necessary
    num_files = math.ceil(file_size/(size_per_file))
    print('File will be split into',num_files,'equal parts')

    # initialize 2D array
    split_data = [[] for i in range(0,num_files)]

    # determine indices of cutoffs in array
    starts = [math.floor(i * data_len/num_files) for i in range(0,num_files)]
    starts.append(data_len)

    # loop through 2D array
    for i in range(0,num_files):
        # loop through each range in array
        for n in range(starts[i],starts[i+1]):
            split_data[i].append(data[n])
        
        # create file when section is complete
        name = os.path.basename(file_name).split('.')[0] + '_' + str(i+1) + '.json'
        with open(name, 'w') as outfile:
            json.dump(split_data[i], outfile)
            
        print('Part',str(i+1),'... completed')

    print('Success! Script Completed')

if __name__ == "__main__":
    json_splitter(file_name="example.json", max_file_size=1024000, del_original=False)