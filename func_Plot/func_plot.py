import matplotlib.pyplot as plt
import numpy as np

#==============================================================
# plt.figure(num=3, figsize=(8, 8))
# Y_sdr = np.arange(0, 100, 0.1)
# Y_hdr = Y_sdr + 100
# plt.title("Inverse Tone Mapping")
# plt.xlabel("SDR luminance")
# plt.ylabel("HDR luminance")
# plt.plot(Y_sdr, Y_hdr, label='v0')
# plt.show()
#---------draw multiple lines in one graph--------
# plt.plot(Y_sdr, Y_hdr_0, label='v0')
# plt.plot(Y_sdr, Y_hdr_1, label='v1')
# plt.plot(Y_sdr, Y_hdr_2, label='v2')
# plt.legend()
# plt.show()

#==============================================================
# plt.figure(num=3, figsize=(8, 8))
# plt.scatter(sdrx_cut2,sdry_cut2,s=1,c='r')
# plt.scatter(sdr2020_xyY[:,:,0],sdr2020_xyY[:,:,1],s=0.1,c='b')
# plt.show()


# plt.figure(num=3, figsize=(8, 8))
# plt.scatter(uv_white_point[0], uv_white_point[1], s=4, c = 'black', label='D65')
# plt.plot(uv_sdr_prima[:,0], uv_sdr_prima[:,1], color='r', label= 'bt.709')
# plt.plot(uv_hdr_prima[:,0], uv_hdr_prima[:,1], color='b', label= 'bt.2020')
# plt.plot((uv_sdr_prima[:,0][0], uv_sdr_prima[:,0][2]), (uv_sdr_prima[:,1][0],uv_sdr_prima[:,1][2]), color='r')
# plt.plot((uv_hdr_prima[:,0][0], uv_hdr_prima[:,0][2]), (uv_hdr_prima[:,1][0],uv_hdr_prima[:,1][2]), color='b')
# plt.legend()
# plt.show()

#--------------------------------------------------------------------------------------
# plt.figure(num=3, figsize=(8, 8))
# plt.title("the distribution of x and y")
# plt.xlabel('CIE x')
# plt.ylabel('CIE y')
# plt.scatter(white_point[0], white_point[1], s=4, c = 'black', label='D65')
# plt.plot(sdr_prima[:,0], sdr_prima[:,1], color='r')
# plt.plot((sdr_prima[:,0][0], sdr_prima[:,0][2]), (sdr_prima[:,1][0],sdr_prima[:,1][2]), color='r', label= 'bt.709')
# plt.plot(hdr_prima[:,0], hdr_prima[:,1], color='b')
# plt.plot((hdr_prima[:,0][0], hdr_prima[:,0][2]), (hdr_prima[:,1][0],hdr_prima[:,1][2]), color='b', label= 'bt.2020')
# # plt.scatter(sdrx_cut,sdry_cut,s=0.1,c='r',label='bt.709')
# # plt.scatter(sdr2020_xyY[:,:,0],sdr2020_xyY[:,:,1],s=0.1,c='b',label='bt.2020')
# plt.legend()
# plt.show()


#---------------2020 and 709 boundraies in Yu'v'-----------------------------
def xy_to_uv( x, y):
    u = (4*x) / (3-2*x+12*y)
    v = (9*y) / (3-2*x+12*y)
    return np.concatenate((u[...,None], v[...,None]),-1)

def plt_gamut(white_point, sdr_prima, hdr_prima, sdr709_xyY, sdr2020_xyY,fig_size=(8, 8), title='x and y', xlabel='x', ylabel='y'):
    plt.figure(num=3, figsize=fig_size)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.scatter(white_point[0], white_point[1], s=4, c = 'black', label='D65')
    plt.plot(sdr_prima[:,0], sdr_prima[:,1], color='r')
    plt.plot((sdr_prima[:,0][0], sdr_prima[:,0][2]), (sdr_prima[:,1][0],sdr_prima[:,1][2]), color='r', label= 'bt.709')
    plt.plot(hdr_prima[:,0], hdr_prima[:,1], color='b')
    plt.plot((hdr_prima[:,0][0], hdr_prima[:,0][2]), (hdr_prima[:,1][0],hdr_prima[:,1][2]), color='b', label= 'bt.2020')
    plt.scatter(sdr709_xyY[:,:,0],sdr709_xyY[:,:,1],s=0.1,c='r',label='bt.709')
    plt.scatter(sdr2020_xyY[:,:,0],sdr2020_xyY[:,:,1],s=0.1,c='b',label='bt.2020')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    hdr_prima = np.array([[ 0.708,  0.292],
                        [ 0.17 ,  0.797],
                        [ 0.131,  0.046]])
    sdr_prima = np.array([[ 0.64,  0.33],
                            [ 0.3 ,  0.6 ],
                            [ 0.15,  0.06]])
    white_point = np.array([ 0.3127,  0.329 ])
    # uv_white_point = xy_to_uv(white_point[0], white_point[1])
    # uv_sdr_prima =  xy_to_uv(sdr_prima[:,0], sdr_prima[:,1])
    # uv_hdr_prima =  xy_to_uv(hdr_prima[:,0], hdr_prima[:,1])

    plt_gamut(white_point, sdr_prima, hdr_prima)