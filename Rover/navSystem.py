import numpy as np

class navsystem(object)
    
    def __init__(self, xy_frames_stored, # number of past x/y/theta readings to remember
            sensor_frames_stored, # number of past 9DOF readings to remember
            encoder_frames_stored, # number of past encoder readings to remember
            zero_angle, # offset for theta
            encoder_distance, # distance of one encoder tick
            skid_err_range): # how much faster the wheels can be than the accelerometers would estimate without the system reporting slippage, as a percentage of accelerometer readings

        zero_angle = zero_angle # offset for theta = 0
        # preallocate arrays
        dx = np.zeros((1,xy_frames_stored), dtype = np.float32)
        dy = np.zeros((1,xy_frames_stored), dtype = np.float32)
        theta = np.zeros((1,xy_frames_stored), dtype = np.float32)
        accel = np.zeros((3,sensor_frames_stored,), dtype = np.float32)
        gyro = np.zeros((3,sensor_frames_stored,), dtype = np.float32)
        mag = np.zeros((3,sensor_frames_stored,), dtype = np.float32)
        encoder = np.zeros((2,encoder_frames_stored,), dtype = np.float32)
        r = np.zeros((1,xy_frames_stored), dtype = int)
        #deprecated for shit encoders
        #encoder_cnt = np.zeros((2,1), dtype = int)  # counts encoder triggers 
        xy_i = 0 # index into x/y/theta
        sensor_i = 0 # index into 9DOF arrays
        encoder_i = 0 # index into past encoders
        v_old = 0 # last measured velocity from 

    def new_9dof(self,full_9dof):
        gyro(sensor_i) = full_9dof(0)
        mag(sensor_i) = full_9dof(1)
        accel(sensor_i) = full_9dof(2)
        sensor_i = (sensor_i + 1) % sensor_frames_stored

    #deprecated  for shit encoders
    #def new_encoder(self,n): # n specifies left or right
    #    encoder_cnt(n) += 1
    def new_encoder(self,full_enc) # expects full_enc as tuple of (L,R)
        encoder(0,encoder_i) = full_enc(0)
        encoder(1,encoder_i) = full_enc(1)
        encoder_i = (encoder_i + 1) % encoder_frames_stored

    def read_displacement(self):
        xy_i = (xy_i + 1) % xy_frames_stored
        r(xy_i) = encoder_cnt(0) * encoder_distance # just use one wheel for efficiency. change this to an average of both wheels if things are weird
        theta(xy_i) = # TODO
        theta_avg = (theta(xy_i) + theta(xy_i-1))/2
        dx(xy_i) = np.cos(theta_avg)*r
        dy(xy_i) = np.sin(theta_avg)*r
        if self.confirm_distance()
            return dx(xy_i),dy(xy_i),theta(xy_i)
        else
            # TODO confirm with Nathan

    def confirm_distance(self):
        return 1 # for now
        # DUMB WAY - a = delta v - only works if >= 1 encoder sample per read_displacement() call
        # skid_err_range depends on this too

        # enc_a = r(xy_i) - r(xy_i-1) 
        # accel_a = np.sum(accel(n,:))/(accel.shape[1]) # TODO fill in n for correct dim - i.e. rover's "fwd"
        #if np.abs(accel_a-enc_a)/(accel_a) > skid_err_range # if error is too large
        # TODO would it be better to use flat error range? i.e. 
        #    return 0
        #else
        #    return 1
        
        # new way - assume that the only errors will be skidding - i.e. wheels report faster speed than accel indicates
        # still using shit encoders though
        # first_nonzero = find(r)[1] # 
        # 
        # v = sum(r[first_nonzero:second_nonzero])/(second_nonzero-first_nonzero)

        # if (v == 1): # when encoder triggers
        #   v_progress = v_old # store last v count 

        # enc_a = v - v_old
        # 
        # accel_a = np.sum(accel(n,:))/(accel.shape[1]) # TODO fill in n for correct dim - i.e. rover's "fwd"

        # v_progress = v

        # if ((enc_a - accel_a) / accel_a > skid_err_range)
        #   return 0
        # else 
        #   return 1 
        # 
