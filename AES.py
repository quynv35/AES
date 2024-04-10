
def chiakhoa(k):
    part_length = len(k) // 4

    parts = [k[i * part_length:(i + 1) * part_length] for i in range(4)]

    return parts
    

def RotWord(k):
    return k[2:]+k[0:2]

def SubWord(word):
    sw = ""
    c = "0123456789abcdef"
    sbox = [
    '63', '7c', '77', '7b', 'f2', '6b', '6f', 'c5', '30', '01', '67', '2b', 'fe', 'd7', 'ab', '76',
    'ca', '82', 'c9', '7d', 'fa', '59', '47', 'f0', 'ad', 'd4', 'a2', 'af', '9c', 'a4', '72', 'c0',
    'b7', 'fd', '93', '26', '36', '3f', 'f7', 'cc', '34', 'a5', 'e5', 'f1', '71', 'd8', '31', '15',
    '04', 'c7', '23', 'c3', '18', '96', '05', '9a', '07', '12', '80', 'e2', 'eb', '27', 'b2', '75',
    '09', '83', '2c', '1a', '1b', '6e', '5a', 'a0', '52', '3b', 'd6', 'b3', '29', 'e3', '2f', '84',
    '53', 'd1', '00', 'ed', '20', 'fc', 'b1', '5b', '6a', 'cb', 'be', '39', '4a', '4c', '58', 'cf',
    'd0', 'ef', 'aa', 'fb', '43', '4d', '33', '85', '45', 'f9', '02', '7f', '50', '3c', '9f', 'a8',
    '51', 'a3', '40', '8f', '92', '9d', '38', 'f5', 'bc', 'b6', 'da', '21', '10', 'ff', 'f3', 'd2',
    'cd', '0c', '13', 'ec', '5f', '97', '44', '17', 'c4', 'a7', '7e', '3d', '64', '5d', '19', '73',
    '60', '81', '4f', 'dc', '22', '2a', '90', '88', '46', 'ee', 'b8', '14', 'de', '5e', '0b', 'db',
    'e0', '32', '3a', '0a', '49', '06', '24', '5c', 'c2', 'd3', 'ac', '62', '91', '95', 'e4', '79',
    'e7', 'c8', '37', '6d', '8d', 'd5', '4e', 'a9', '6c', '56', 'f4', 'ea', '65', '7a', 'ae', '08',
    'ba', '78', '25', '2e', '1c', 'a6', 'b4', 'c6', 'e8', 'dd', '74', '1f', '4b', 'bd', '8b', '8a',
    '70', '3e', 'b5', '66', '48', '03', 'f6', '0e', '61', '35', '57', 'b9', '86', 'c1', '1d', '9e',
    'e1', 'f8', '98', '11', '69', 'd9', '8e', '94', '9b', '1e', '87', 'e9', 'ce', '55', '28', 'df',
    '8c', 'a1', '89', '0d', 'bf', 'e6', '42', '68', '41', '99', '2d', '0f', 'b0', '54', 'bb', '16'
    ]
    
    part_length = len(word) // 4
    parts = [word[i * part_length:(i + 1) * part_length] for i in range(4)]
    for i in parts:
        a = c.index(i[0]) * 16
        b = c.index(i[1])
        index = a+b
        sw += sbox[index]
    return sw

def XorRcon(sw,j):
    Rcon = ['00', '01', '02', '04', '08', '10', '20', '40', '80', '1b', '36']
    rcon = f"{Rcon[j]}000000"
    result = XorRbit(rcon,sw)
    return result

def XorRbit(str1, str2):
    bytes1 = bytes.fromhex(str1)
    bytes2 = bytes.fromhex(str2)
    result_bytes = bytes(a ^ b for a, b in zip(bytes1, bytes2))
    return result_bytes.hex()

key = "2b7e151628aed2a6abf7158809cf4f3c"

def sinhkhoa(key,i):
    w0,w1,w2,w3=chiakhoa(key)
    rw = RotWord(w3)
    sw = SubWord(rw) 
    xcsw = XorRcon(sw,i)
    w4 = XorRbit(xcsw, w0) 
    w5 = XorRbit(w1,w4)
    w6 = XorRbit(w2,w5)
    w7 = XorRbit(w3,w6)
    K = w4+w5+w6+w7
    return(K)

K1 = sinhkhoa(key,1)
K2 = sinhkhoa(K1,2)
K3 = sinhkhoa(K2,3)
K4 = sinhkhoa(K3,4)
K5 = sinhkhoa(K4,5)
K6 = sinhkhoa(K5,6)
K7 = sinhkhoa(K6,7)
K8 = sinhkhoa(K7,8)
K9 = sinhkhoa(K8,9)
K10 = sinhkhoa(K9,10)

print(K10) #d014f9a8c9ee2589e13f0cc8b6630ca6

