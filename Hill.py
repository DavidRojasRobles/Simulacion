import random
import itertools as it
import numpy as np
# # import pandas as pd
# # import matplotlib.pyplot as plt
# # %matplotlib inline
# # pd.__version__
#
# alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#
# print alphabet[0]
#
# def hillDecypher(key, numbers):
#         mat = list()
#         if (numbers):
#             mat = toMatrixHorizontalNumbers(key, alphabet)
#         else:
#             mat = toMatrixHorizontal(key, alphabet)
#
#         hillDecypherMat(mat)
#
#
# def hillDecypherMat(mat):
#     if (validateHC(key, alphabet)) :
#             c =  messageWithKeyMatrix(key, content, alphabet) if (contInd == null) else contInd; //makes sure message is matrix
#             int det = this.det(key); //Finds determinant of key
#             double[][] d = this.matrixToDouble(key); //makes key double
# //            MatrixUtils.inverse(MatrixUtils.createRealMatrix(d));
# //            int[][] invKey = this.matrixToInt(MatrixUtils.inverse(MatrixUtils.createRealMatrix(d)).getData());
#             int[][] invKey = this.invert2by2Matrix(key);//{{15, -11}, {-8, 5}};
#             int inv = this.findInv(this.loop(det % this.alphabet.length(), this.alphabet.length()), this.alphabet.length()); //Finds inverse of det%27
#
#             for (int i = 0; i < invKey.length; i++) {
#                 for (int j = 0; j < invKey[1].length; j++) {
#                     invKey[i][j] = this.loop(invKey[i][j] % this.alphabet.length(), this.alphabet.length());
#                 }
#             }
#
#             for (int i = 0; i < invKey.length; i++) {
#                 for (int j = 0; j < invKey[1].length; j++) {
#                     invKey[i][j] = this.loop((inv * invKey[i][j]) % this.alphabet.length(), this.alphabet.length());
#                 }
#             }
#
#             int[][] mk = this.multiply(invKey, c);
#
#             for (int i = 0; i < mk.length; i++) {
#                 for (int j = 0; j < mk[1].length; j++) {
#                     mk[i][j] = mk[i][j] % this.alphabet.length();
#                 }
#             }
#
# //           this.printMatrix(mk);
#             char[] res = new char[mk.length * mk[1].length];
#             int count = 0;
#             for (int i = 0; i < mk[1].length; i++) {
#                 for (int j = 0; j < mk.length; j++) {
#                     res[count] = this.alphabet.charAt(mk[j][i]);
#                     count++;
#                 }
#             }
#
#             String msgCy = new String(res);
#             System.out.println("\nThe decyphered message is: " + msgCy);
# //
#         } else {
#             System.out.println("La clave no es valida.");


mat = [[]]
