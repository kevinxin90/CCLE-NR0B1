'''extract NSCLC cell line information from the database'''


def NSCLC_extractor(title):
    NSCLC_title = []
    for _item in title:
        cell_type1 = _item.split('_')[2]
        cell_type6 = _item.split('_')[2].split('.')[0]
        cell_type7 = _item.split('_')[2].split(',')[0]
        if cell_type1 == 'Large':
            NSCLC_cell_type = ['Non-Small', 'Large', 'Adenocarcinoma',
                               'Squamous']
            cell_type2 = _item.split('_')[4].split(':')[0]
            cell_type3 = cell_type2.split('.')[0]
            cell_type4 = cell_type2.split(',')[0]
            cell_type5 = cell_type2.split('.')[-1]
            cell_type_sum = [cell_type3, cell_type4, cell_type5]
            if (cell_type3 in NSCLC_cell_type) | \
               (cell_type4 in NSCLC_cell_type) | \
               (cell_type5 in NSCLC_cell_type):
                NSCLC_title.append(_item)
                print _item
                print True
            else:
                print _item
                print False
        elif (cell_type6 in NSCLC_cell_type) | (cell_type7 in NSCLC_cell_type):
            NSCLC_title.append(_item)
            print _item
            print True
        else:
            print _item
            print False
    return NSCLC_title


'''parse unique NSCLC cell line names from the extracted NSCLC database'''


def parse_unique_cell_line_name(NSCLC_title):
    NSCLC_cell_line = []
    for _item in NSCLC_title:
        if _item.split('_')[2] == 'Large':
            NSCLC_cell_line.append(_item.split('_')[3])
        else:
            NSCLC_cell_line.append(_item.split('_')[2])
    unique_NSCLC_cell_line = list(set(NSCLC_cell_line))
    return (NSCLC_cell_line, unique_NSCLC_cell_line)


''' return the column numbers of duplicate cell lines '''


def column_assemble(my_list, unique_title):
    dict = {}
    for item in unique_title:
        dict[item] = [i for i, x in enumerate(my_list) if x == item]
    return dict


'''return the matrix of which the row max is higher than matrix mean'''


def matrix_normal(matrix):
    matrix_normal = matrix[numpy.amax(matrix, axis=1) > matrix.mean()]
    return matrix_normal
