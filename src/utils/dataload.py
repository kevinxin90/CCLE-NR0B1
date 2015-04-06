
'''open file and extract the first line as title'''


def get_title(file_name):
    data = csv.reader(open(file_name, 'rU'), delimiter=',')
    title = data.next()
    # the first item is 'gene', should be dismissed
    title = title[1:]
    return title

'''read in data, remove first line(title), return
all numeric value as matrix and gene_IDs'''


def numpy_read(file_name):
    data = csv.reader(open(file_name, 'rU'), delimiter=',')
    col_num = len(data.next())-1
    row_num = sum(1 for row in data)
    matrix = numpy.ndarray([row_num, col_num])
    gene_ID = []
    data = csv.reader(open(file_name, 'rU'), delimiter=',')
    title = data.next()
    for ii, row in enumerate(data):
        matrix[ii] = row[1:]
        gene_ID.append(row[0])
    return (row_num, matrix, gene_ID)
