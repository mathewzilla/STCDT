"""
Test data for the Spike-Train Communities algorithm (Humphries, 2011).

Thomas Sharp, 2013
thomas.sharp@riken.jp
"""
import numpy

n_trains = 105
train_period = 1. # in seconds

# Trial ID, Time (seconds)
spikes = numpy.array([[1.0000, 0.0428],
                      [1.0000, 0.0434],
                      [1.0000, 0.3604],
                      [1.0000, 0.4222],
                      [1.0000, 0.4938],
                      [1.0000, 0.7899],
                      [1.0000, 0.8535],
                      [1.0000, 0.8954],
                      [1.0000, 0.9092],
                      [1.0000, 0.9094],
                      [2.0000, 0.0421],
                      [2.0000, 0.0452],
                      [2.0000, 0.0814],
                      [2.0000, 0.3604],
                      [2.0000, 0.9093],
                      [2.0000, 0.9818],
                      [3.0000, 0.0431],
                      [3.0000, 0.2333],
                      [3.0000, 0.3601],
                      [3.0000, 0.8528],
                      [3.0000, 0.9105],
                      [4.0000, 0.0149],
                      [4.0000, 0.5147],
                      [4.0000, 0.6582],
                      [4.0000, 0.8864],
                      [4.0000, 0.9362],
                      [4.0000, 0.9779],
                      [5.0000, 0.0157],
                      [5.0000, 0.0189],
                      [5.0000, 0.0321],
                      [5.0000, 0.0965],
                      [5.0000, 0.1199],
                      [5.0000, 0.6585],
                      [5.0000, 0.8440],
                      [5.0000, 0.8859],
                      [6.0000, 0.0405],
                      [6.0000, 0.0448],
                      [6.0000, 0.3605],
                      [6.0000, 0.8541],
                      [7.0000, 0.0161],
                      [7.0000, 0.0344],
                      [7.0000, 0.1301],
                      [7.0000, 0.2138],
                      [7.0000, 0.6582],
                      [7.0000, 0.8884],
                      [7.0000, 0.9779],
                      [8.0000, 0.1266],
                      [8.0000, 0.2294],
                      [8.0000, 0.2495],
                      [8.0000, 0.3208],
                      [8.0000, 0.3838],
                      [8.0000, 0.7961],
                      [8.0000, 0.9325],
                      [8.0000, 0.9484],
                      [9.0000, 0.2413],
                      [9.0000, 0.2476],
                      [9.0000, 0.2660],
                      [9.0000, 0.2823],
                      [9.0000, 0.3211],
                      [9.0000, 0.3866],
                      [9.0000, 0.8044],
                      [9.0000, 0.8381],
                      [9.0000, 0.9329],
                      [10.0000, 0.0156],
                      [10.0000, 0.2590],
                      [10.0000, 0.2903],
                      [10.0000, 0.6568],
                      [10.0000, 0.9790],
                      [11.0000, 0.0169],
                      [11.0000, 0.0316],
                      [11.0000, 0.0342],
                      [11.0000, 0.0731],
                      [11.0000, 0.1051],
                      [11.0000, 0.1709],
                      [11.0000, 0.5585],
                      [11.0000, 0.8880],
                      [11.0000, 0.9768],
                      [12.0000, 0.0443],
                      [12.0000, 0.0461],
                      [12.0000, 0.3609],
                      [12.0000, 0.4354],
                      [12.0000, 0.8530],
                      [12.0000, 0.9089],
                      [13.0000, 0.0156],
                      [13.0000, 0.0349],
                      [13.0000, 0.1967],
                      [13.0000, 0.3498],
                      [13.0000, 0.6590],
                      [13.0000, 0.9782],
                      [14.0000, 0.0168],
                      [14.0000, 0.0342],
                      [14.0000, 0.6562],
                      [14.0000, 0.9766],
                      [15.0000, 0.0087],
                      [15.0000, 0.1279],
                      [15.0000, 0.2473],
                      [15.0000, 0.3193],
                      [15.0000, 0.3838],
                      [15.0000, 0.3927],
                      [15.0000, 0.8691],
                      [15.0000, 0.9328],
                      [16.0000, 0.1150],
                      [16.0000, 0.1260],
                      [16.0000, 0.2470],
                      [16.0000, 0.3203],
                      [16.0000, 0.3553],
                      [16.0000, 0.3836],
                      [16.0000, 0.8907],
                      [16.0000, 0.9323],
                      [17.0000, 0.0164],
                      [17.0000, 0.0344],
                      [17.0000, 0.5031],
                      [17.0000, 0.6584],
                      [17.0000, 0.8883],
                      [17.0000, 0.9787],
                      [18.0000, 0.0463],
                      [18.0000, 0.1275],
                      [18.0000, 0.2473],
                      [18.0000, 0.3183],
                      [18.0000, 0.3835],
                      [18.0000, 0.9317],
                      [19.0000, 0.0166],
                      [19.0000, 0.0332],
                      [19.0000, 0.0374],
                      [19.0000, 0.6565],
                      [19.0000, 0.8882],
                      [19.0000, 0.9776],
                      [20.0000, 0.0416],
                      [20.0000, 0.0445],
                      [20.0000, 0.2123],
                      [20.0000, 0.3607],
                      [20.0000, 0.8538],
                      [20.0000, 0.9086],
                      [20.0000, 0.9829],
                      [21.0000, 0.1279],
                      [21.0000, 0.2492],
                      [21.0000, 0.3190],
                      [21.0000, 0.3845],
                      [21.0000, 0.9330],
                      [22.0000, 0.1249],
                      [22.0000, 0.2492],
                      [22.0000, 0.3192],
                      [22.0000, 0.3848],
                      [22.0000, 0.7676],
                      [22.0000, 0.7709],
                      [22.0000, 0.9328],
                      [22.0000, 0.9498],
                      [23.0000, 0.0167],
                      [23.0000, 0.0332],
                      [23.0000, 0.0845],
                      [23.0000, 0.2881],
                      [23.0000, 0.5054],
                      [23.0000, 0.8856],
                      [24.0000, 0.0170],
                      [24.0000, 0.0358],
                      [24.0000, 0.3476],
                      [24.0000, 0.6562],
                      [24.0000, 0.8878],
                      [24.0000, 0.9778],
                      [25.0000, 0.0421],
                      [25.0000, 0.0448],
                      [25.0000, 0.3612],
                      [25.0000, 0.8547],
                      [25.0000, 0.9082],
                      [26.0000, 0.0328],
                      [26.0000, 0.6576],
                      [26.0000, 0.7082],
                      [26.0000, 0.8861],
                      [26.0000, 0.9776],
                      [27.0000, 0.0265],
                      [27.0000, 0.2482],
                      [27.0000, 0.3203],
                      [27.0000, 0.3844],
                      [28.0000, 0.2480],
                      [28.0000, 0.3202],
                      [28.0000, 0.3854],
                      [28.0000, 0.6919],
                      [28.0000, 0.9317],
                      [29.0000, 0.0414],
                      [29.0000, 0.0456],
                      [29.0000, 0.1781],
                      [29.0000, 0.2487],
                      [29.0000, 0.3603],
                      [29.0000, 0.8540],
                      [29.0000, 0.9078],
                      [30.0000, 0.0423],
                      [30.0000, 0.0442],
                      [30.0000, 0.3616],
                      [30.0000, 0.4925],
                      [30.0000, 0.6630],
                      [30.0000, 0.8532],
                      [30.0000, 0.9084],
                      [31.0000, 0.1254],
                      [31.0000, 0.2484],
                      [31.0000, 0.3844],
                      [31.0000, 0.3999],
                      [31.0000, 0.4993],
                      [31.0000, 0.7103],
                      [31.0000, 0.7110],
                      [31.0000, 0.7285],
                      [31.0000, 0.9335],
                      [32.0000, 0.0175],
                      [32.0000, 0.0353],
                      [32.0000, 0.1622],
                      [32.0000, 0.6576],
                      [32.0000, 0.8898],
                      [32.0000, 0.9777],
                      [33.0000, 0.0430],
                      [33.0000, 0.0441],
                      [33.0000, 0.1327],
                      [33.0000, 0.3606],
                      [33.0000, 0.5464],
                      [33.0000, 0.6346],
                      [33.0000, 0.8528],
                      [33.0000, 0.9033],
                      [33.0000, 0.9079],
                      [34.0000, 0.0151],
                      [34.0000, 0.0337],
                      [34.0000, 0.3262],
                      [34.0000, 0.5051],
                      [34.0000, 0.6583],
                      [34.0000, 0.8863],
                      [34.0000, 0.9784],
                      [35.0000, 0.0418],
                      [35.0000, 0.3606],
                      [35.0000, 0.8543],
                      [35.0000, 0.8841],
                      [35.0000, 0.9093],
                      [36.0000, 0.1269],
                      [36.0000, 0.2480],
                      [36.0000, 0.3080],
                      [36.0000, 0.3185],
                      [36.0000, 0.3835],
                      [36.0000, 0.9320],
                      [37.0000, 0.0448],
                      [37.0000, 0.0449],
                      [37.0000, 0.3600],
                      [37.0000, 0.7255],
                      [37.0000, 0.8541],
                      [37.0000, 0.9089],
                      [38.0000, 0.0163],
                      [38.0000, 0.0340],
                      [38.0000, 0.4236],
                      [38.0000, 0.6582],
                      [38.0000, 0.8869],
                      [38.0000, 0.9782],
                      [39.0000, 0.0156],
                      [39.0000, 0.0335],
                      [39.0000, 0.1940],
                      [39.0000, 0.5669],
                      [39.0000, 0.6571],
                      [39.0000, 0.8867],
                      [40.0000, 0.0652],
                      [40.0000, 0.1262],
                      [40.0000, 0.2480],
                      [40.0000, 0.3858],
                      [40.0000, 0.9334],
                      [41.0000, 0.0172],
                      [41.0000, 0.0455],
                      [41.0000, 0.6583],
                      [41.0000, 0.7443],
                      [41.0000, 0.8188],
                      [41.0000, 0.9782],
                      [42.0000, 0.1270],
                      [42.0000, 0.2476],
                      [42.0000, 0.3006],
                      [42.0000, 0.3218],
                      [42.0000, 0.3846],
                      [43.0000, 0.0165],
                      [43.0000, 0.0331],
                      [43.0000, 0.6586],
                      [43.0000, 0.8877],
                      [44.0000, 0.0431],
                      [44.0000, 0.0446],
                      [44.0000, 0.3598],
                      [44.0000, 0.3867],
                      [44.0000, 0.8536],
                      [44.0000, 0.9061],
                      [45.0000, 0.0448],
                      [45.0000, 0.3607],
                      [45.0000, 0.4941],
                      [45.0000, 0.8533],
                      [45.0000, 0.9103],
                      [46.0000, 0.0170],
                      [46.0000, 0.0327],
                      [46.0000, 0.7986],
                      [46.0000, 0.8857],
                      [46.0000, 0.9769],
                      [46.0000, 0.9791],
                      [47.0000, 0.0169],
                      [47.0000, 0.0332],
                      [47.0000, 0.1285],
                      [47.0000, 0.2008],
                      [47.0000, 0.2595],
                      [47.0000, 0.2969],
                      [47.0000, 0.6583],
                      [48.0000, 0.0425],
                      [48.0000, 0.0427],
                      [48.0000, 0.3604],
                      [48.0000, 0.8531],
                      [48.0000, 0.9092],
                      [49.0000, 0.0187],
                      [49.0000, 0.0359],
                      [49.0000, 0.1024],
                      [49.0000, 0.1542],
                      [49.0000, 0.8889],
                      [49.0000, 0.9783],
                      [50.0000, 0.0445],
                      [50.0000, 0.0448],
                      [50.0000, 0.3611],
                      [50.0000, 0.8531],
                      [50.0000, 0.9105],
                      [50.0000, 0.9120],
                      [51.0000, 0.3855],
                      [51.0000, 0.4952],
                      [52.0000, 0.0446],
                      [52.0000, 0.3597],
                      [52.0000, 0.5198],
                      [52.0000, 0.9080],
                      [53.0000, 0.0354],
                      [53.0000, 0.6573],
                      [53.0000, 0.7069],
                      [53.0000, 0.9784],
                      [54.0000, 0.0454],
                      [54.0000, 0.3599],
                      [54.0000, 0.8536],
                      [54.0000, 0.9095],
                      [55.0000, 0.0339],
                      [55.0000, 0.6576],
                      [55.0000, 0.8798],
                      [55.0000, 0.9786],
                      [56.0000, 0.0429],
                      [56.0000, 0.0445],
                      [56.0000, 0.3117],
                      [56.0000, 0.3624],
                      [56.0000, 0.4427],
                      [56.0000, 0.8546],
                      [56.0000, 0.9101],
                      [57.0000, 0.0169],
                      [57.0000, 0.0348],
                      [57.0000, 0.3982],
                      [57.0000, 0.6427],
                      [57.0000, 0.6558],
                      [57.0000, 0.8451],
                      [57.0000, 0.8876],
                      [57.0000, 0.9783],
                      [57.0000, 0.9934],
                      [58.0000, 0.1388],
                      [58.0000, 0.2488],
                      [58.0000, 0.3202],
                      [58.0000, 0.3849],
                      [58.0000, 0.5195],
                      [58.0000, 0.8578],
                      [58.0000, 0.9335],
                      [59.0000, 0.2480],
                      [59.0000, 0.3203],
                      [59.0000, 0.3405],
                      [59.0000, 0.3858],
                      [59.0000, 0.7118],
                      [59.0000, 0.9315],
                      [60.0000, 0.0429],
                      [60.0000, 0.0441],
                      [60.0000, 0.3604],
                      [61.0000, 0.1283],
                      [61.0000, 0.2490],
                      [61.0000, 0.3198],
                      [61.0000, 0.3833],
                      [61.0000, 0.9339],
                      [62.0000, 0.0161],
                      [62.0000, 0.0369],
                      [62.0000, 0.6586],
                      [62.0000, 0.8883],
                      [62.0000, 0.9779],
                      [63.0000, 0.1009],
                      [63.0000, 0.2486],
                      [63.0000, 0.2579],
                      [63.0000, 0.3211],
                      [63.0000, 0.3836],
                      [63.0000, 0.7775],
                      [63.0000, 0.9331],
                      [64.0000, 0.1268],
                      [64.0000, 0.2500],
                      [64.0000, 0.3181],
                      [64.0000, 0.3843],
                      [64.0000, 0.9339],
                      [65.0000, 0.0169],
                      [65.0000, 0.6584],
                      [65.0000, 0.8877],
                      [65.0000, 0.9419],
                      [65.0000, 0.9790],
                      [66.0000, 0.0408],
                      [66.0000, 0.0445],
                      [66.0000, 0.3608],
                      [66.0000, 0.8523],
                      [66.0000, 0.9086],
                      [66.0000, 0.9186],
                      [67.0000, 0.0421],
                      [67.0000, 0.0472],
                      [67.0000, 0.3588],
                      [67.0000, 0.4347],
                      [67.0000, 0.5685],
                      [67.0000, 0.6399],
                      [67.0000, 0.9093],
                      [68.0000, 0.0160],
                      [68.0000, 0.0333],
                      [68.0000, 0.4923],
                      [68.0000, 0.6589],
                      [68.0000, 0.8879],
                      [68.0000, 0.9699],
                      [68.0000, 0.9765],
                      [69.0000, 0.0264],
                      [69.0000, 0.0450],
                      [69.0000, 0.1432],
                      [69.0000, 0.3595],
                      [69.0000, 0.8532],
                      [69.0000, 0.9098],
                      [70.0000, 0.0163],
                      [70.0000, 0.8892],
                      [70.0000, 0.8922],
                      [70.0000, 0.9777],
                      [71.0000, 0.0357],
                      [71.0000, 0.0915],
                      [71.0000, 0.3473],
                      [71.0000, 0.6352],
                      [71.0000, 0.6575],
                      [71.0000, 0.8873],
                      [71.0000, 0.9776],
                      [71.0000, 0.9936],
                      [72.0000, 0.1992],
                      [72.0000, 0.2483],
                      [72.0000, 0.3186],
                      [72.0000, 0.3862],
                      [72.0000, 0.9316],
                      [72.0000, 0.9370],
                      [73.0000, 0.0416],
                      [73.0000, 0.0424],
                      [73.0000, 0.3596],
                      [73.0000, 0.4435],
                      [73.0000, 0.5472],
                      [73.0000, 0.8543],
                      [73.0000, 0.9095],
                      [74.0000, 0.0423],
                      [74.0000, 0.0433],
                      [74.0000, 0.8529],
                      [74.0000, 0.9093],
                      [75.0000, 0.0423],
                      [75.0000, 0.3281],
                      [75.0000, 0.3598],
                      [75.0000, 0.7813],
                      [75.0000, 0.8531],
                      [75.0000, 0.9089],
                      [76.0000, 0.0428],
                      [76.0000, 0.0439],
                      [76.0000, 0.6255],
                      [76.0000, 0.7332],
                      [76.0000, 0.8531],
                      [77.0000, 0.1279],
                      [77.0000, 0.2473],
                      [77.0000, 0.3181],
                      [77.0000, 0.3843],
                      [77.0000, 0.9297],
                      [78.0000, 0.1271],
                      [78.0000, 0.2481],
                      [78.0000, 0.3113],
                      [78.0000, 0.3201],
                      [78.0000, 0.3832],
                      [78.0000, 0.9305],
                      [79.0000, 0.0423],
                      [79.0000, 0.0433],
                      [79.0000, 0.6715],
                      [79.0000, 0.6770],
                      [79.0000, 0.8553],
                      [79.0000, 0.8765],
                      [80.0000, 0.0420],
                      [80.0000, 0.0454],
                      [80.0000, 0.3615],
                      [80.0000, 0.9084],
                      [81.0000, 0.0084],
                      [81.0000, 0.0418],
                      [81.0000, 0.0453],
                      [81.0000, 0.3597],
                      [81.0000, 0.5192],
                      [81.0000, 0.5540],
                      [81.0000, 0.8533],
                      [81.0000, 0.9094],
                      [81.0000, 0.9643],
                      [82.0000, 0.1265],
                      [82.0000, 0.2049],
                      [82.0000, 0.2471],
                      [82.0000, 0.3848],
                      [82.0000, 0.9317],
                      [83.0000, 0.0341],
                      [83.0000, 0.8880],
                      [83.0000, 0.9783],
                      [84.0000, 0.1261],
                      [84.0000, 0.2205],
                      [84.0000, 0.3185],
                      [84.0000, 0.3847],
                      [84.0000, 0.3896],
                      [84.0000, 0.5312],
                      [84.0000, 0.8572],
                      [84.0000, 0.9336],
                      [85.0000, 0.0441],
                      [85.0000, 0.0447],
                      [85.0000, 0.3595],
                      [85.0000, 0.4862],
                      [85.0000, 0.5558],
                      [85.0000, 0.8540],
                      [85.0000, 0.8730],
                      [85.0000, 0.9101],
                      [86.0000, 0.1288],
                      [86.0000, 0.2481],
                      [86.0000, 0.3206],
                      [86.0000, 0.3857],
                      [86.0000, 0.9313],
                      [87.0000, 0.1272],
                      [87.0000, 0.3208],
                      [87.0000, 0.3836],
                      [87.0000, 0.6688],
                      [88.0000, 0.0157],
                      [88.0000, 0.0346],
                      [88.0000, 0.8877],
                      [88.0000, 0.9772],
                      [89.0000, 0.1261],
                      [89.0000, 0.2496],
                      [89.0000, 0.3193],
                      [89.0000, 0.9319],
                      [90.0000, 0.1262],
                      [90.0000, 0.2488],
                      [90.0000, 0.3190],
                      [90.0000, 0.4553],
                      [90.0000, 0.4893],
                      [90.0000, 0.6171],
                      [90.0000, 0.9329],
                      [91.0000, 0.0433],
                      [91.0000, 0.0436],
                      [91.0000, 0.3596],
                      [91.0000, 0.7243],
                      [91.0000, 0.8549],
                      [91.0000, 0.9107],
                      [92.0000, 0.2472],
                      [92.0000, 0.3203],
                      [92.0000, 0.3848],
                      [92.0000, 0.9329],
                      [93.0000, 0.1275],
                      [93.0000, 0.3223],
                      [93.0000, 0.3340],
                      [93.0000, 0.3856],
                      [93.0000, 0.9341],
                      [94.0000, 0.1260],
                      [94.0000, 0.2479],
                      [94.0000, 0.3205],
                      [94.0000, 0.3837],
                      [94.0000, 0.4799],
                      [94.0000, 0.5842],
                      [94.0000, 0.9259],
                      [94.0000, 0.9323],
                      [95.0000, 0.1273],
                      [95.0000, 0.3208],
                      [95.0000, 0.3831],
                      [95.0000, 0.3908],
                      [95.0000, 0.9343],
                      [96.0000, 0.1267],
                      [96.0000, 0.2485],
                      [96.0000, 0.3194],
                      [96.0000, 0.6460],
                      [96.0000, 0.9324],
                      [96.0000, 0.9892],
                      [97.0000, 0.0151],
                      [97.0000, 0.0330],
                      [97.0000, 0.0868],
                      [97.0000, 0.0892],
                      [97.0000, 0.3649],
                      [97.0000, 0.4658],
                      [97.0000, 0.6558],
                      [97.0000, 0.8879],
                      [97.0000, 0.9770],
                      [98.0000, 0.0165],
                      [98.0000, 0.0338],
                      [98.0000, 0.5775],
                      [98.0000, 0.6934],
                      [98.0000, 0.8132],
                      [98.0000, 0.8868],
                      [98.0000, 0.9792],
                      [99.0000, 0.0425],
                      [99.0000, 0.0451],
                      [99.0000, 0.3601],
                      [99.0000, 0.7458],
                      [99.0000, 0.9076],
                      [100.0000, 0.0410],
                      [100.0000, 0.0439],
                      [100.0000, 0.3615],
                      [100.0000, 0.4564],
                      [100.0000, 0.8529],
                      [100.0000, 0.9094],
                      [101.0000, 0.1257],
                      [101.0000, 0.2482],
                      [101.0000, 0.2963],
                      [101.0000, 0.3837],
                      [101.0000, 0.9321],
                      [102.0000, 0.0169],
                      [102.0000, 0.0342],
                      [102.0000, 0.6585],
                      [102.0000, 0.8878],
                      [103.0000, 0.3220],
                      [103.0000, 0.3845],
                      [103.0000, 0.9333],
                      [104.0000, 0.0172],
                      [104.0000, 0.0337],
                      [104.0000, 0.6580],
                      [104.0000, 0.7495],
                      [104.0000, 0.8878],
                      [104.0000, 0.9540],
                      [104.0000, 0.9788],
                      [105.0000, 0.0433],
                      [105.0000, 0.0440],
                      [105.0000, 0.1378],
                      [105.0000, 0.1487],
                      [105.0000, 0.3616],
                      [105.0000, 0.8542],
                      [105.0000, 0.9080]])