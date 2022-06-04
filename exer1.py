#!/usr/bin/python3

#Exercise1. Modifiy print_matrix1 function to generate the same matrix found in:
#https://upload.wikimedia.org/wikipedia/commons/2/28/Smith-Waterman-Algorithm-Example-Step2.png
#or like sw.PNG

def print_matrix1(a,x,y):
	
	newx='  '+x
	newy='  '+y
	mrows = len(newx)
	ncols = len(newy)

	print(newy)
	for i in range(mrows):
		for j in range(ncols):
			if (i==0):
				print(newy[j], end='  ')
			elif(j==0):
				print(newx[i], end=' ')
			else:
			 	print("%2d" % a[i-1][j-1], end=' ')	
			
		print()


def gen_matrix(x, y, match_score=3, gap_cost=2):
	mrows = len(x)
	ncols = len(y)

	#initialize matrix to zeroes
	a = [0] * (mrows + 1)
	for i in range(mrows + 1):
		a[i] = [0] * (ncols + 1)
	
	#print_matrix(a,x,y)
	
	for i in range(1,mrows+1):
		for j in range(1,ncols+1):
			match = a[i-1][j-1] - match_score
			if(x[i-1] == y[j-1]):
				match = a[i-1][j-1] + match_score
			delete = a[i - 1][j] - gap_cost
			insert = a[i][j - 1] - gap_cost
			a[i][j]=max(match,delete,insert,0)


	#print_matrix(a,x,y)	
	return(a)

# def traceback(a,x,y):
# 	mrows = len(x)
# 	ncols = len(y)
# 	for i in range(mrows,0,-1):
# 		for j in range(ncols,0,-1):
# 				#print("indeice",i,j,end=' ')
# 			if(a[i][j]!=0):
# 				print("%2d" % a[i][j], end=' ')	
			
def traceback(score_matrix, start_pos,seq1,seq2): #adapted from https://gist.github.com/radaniba/11019717

    END, DIAG, UP, LEFT = range(4)
    aligned_seq1 = []
    aligned_seq2 = []
    x, y         = start_pos
    move         = next_move(score_matrix, x, y) #depends the next move 
    print(seq2,len(seq2))
    print(seq1,len(seq1))
    while move != END:
        # print(seq1[x-1],seq2[y-1],move)
        if move == DIAG:
            if(seq1[x-1]==seq2[y-1]): #inroder to store the right sequence  if the seq1 matches sequence 2 it will write the corresponding symbol		
                aligned_seq1.append(seq1[x - 1])
                aligned_seq2.append(seq2[y - 1])
            else: 			
                aligned_seq1.append('')
                aligned_seq2.append('')			
            x -= 1
            y -= 1
        elif move == UP:
            if(seq1[x-1]==seq2[y-1]):
                aligned_seq1.append(seq1[x - 1])
                aligned_seq2.append('')
            else:			
                aligned_seq1.append(seq1[x - 1])
                aligned_seq2.append('-')
            x -= 1
        else:
            aligned_seq1.append(' ')
            aligned_seq2.append(seq2[y - 1])
            y -= 1

        move = next_move(score_matrix, x, y)

    aligned_seq1.append(seq1[x - 1])
    aligned_seq2.append(seq1[y - 1])

    return ''.join(reversed(aligned_seq1)), ''.join(reversed(aligned_seq2))


def next_move(score_matrix, x, y): # this dictates the next move dependeing on the score matrix 
    diag = score_matrix[x - 1][y - 1]
    up   = score_matrix[x - 1][y]
    left = score_matrix[x][y - 1]
    if diag >= up and diag >= left:     # Tie goes to the DIAG move.
        return 1 if diag != 0 else 0    # 1 signals a DIAG move. 0 signals the end.
    elif up > diag and up >= left:      # Tie goes to UP move.
        return 2 if up != 0 else 0      # UP move or end.
    elif left > diag and left > up:
        return 3 if left != 0 else 0    # LEFT move or end.
    else:
        # Execution should not reach here.
        raise ValueError('invalid move during traceback')
			
	

x = "GGTTGACTA"	
y = "TGTTACGG"

a=gen_matrix(x,y)

print_matrix1(a,x,y)
res=traceback(a,(len(x),len(y)),x,y)
print(res[0],end='\n')
print(res[1],end='\n')