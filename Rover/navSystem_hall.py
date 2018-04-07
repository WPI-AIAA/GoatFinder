import numpy as np

class navsystem(object):
    
    def __init__(self, xy_frames_stored, # number of past x/y/theta readings to remember
            sensor_frames_stored, # number of past 9DOF readings to remember
            encoder_frames_stored, # number of past encoder readings to remember
            zero_angle, # offset for theta
            encoder_distance, # distance of one encoder tick
            skid_err_range, # how much faster the wheels can be than the accelerometers would estimate without the system reporting slippage, as a percentage of accelerometer readings
            accel_time_step, # time between acclerometer readings, required as a factor for the reimann sum to calculate velocity
            gyro_pitch_axis # should be Y or 1 for PCB version
            ):

        zero_angle = zero_angle # offset for theta = 0
        # preallocate arrays
        #dx = np.zeros((1,xy_frames_stored), dtype = np.float32)
        #dy = np.zeros((1,xy_frames_stored), dtype = np.float32)
        #theta = np.zeros((1,xy_frames_stored), dtype = np.float32) # unneeded
        accel = np.zeros((3,sensor_frames_stored,), dtype = np.float32)
        gyro = np.zeros((3,sensor_frames_stored,), dtype = np.float32)
        heading = np.zeros((1,sensor_frames_stored,), dtype = np.float32) # abstracted from gyro
        mag = np.zeros((3,sensor_frames_stored,), dtype = np.float32)
        encoder = np.zeros((2,encoder_frames_stored,), dtype = np.float32)
        encoder_cnt = np.zeros(2, dtype = int)
        #r = np.zeros((1,xy_frames_stored), dtype = int)
        #xy_i = 0 # index into x/y/theta
        sensor_i = 0 # index into 9DOF arrays
        sensor_last_i = 0 # last index already read
        encoder_i = 0 # index into past encoders
        v_old = 0 # last measured velocity 
        dt = 0.1 # TODO fill this - 

    def new_9dof(self,full_9dof):
        gyro[:,sensor_i] = full_9dof[0][:]
        mag[:,sensor_i] = full_9d0f[1][:]
        accel[sensor_i] = full_9dof[2][:]
        sensor_i = (sensor_i + 1) % sensor_frames_stored

    def new_encoder(self,n): # n specifies left or right
        encoder_cnt[n] += 1

    def read_displacement(self):

        #create list of new acceleration readings and number of time steps
        if (sensor_i > sensor_last_i): # if array has not looped around
            new_accels = accel[:, sensor_last_i+1:sensor_i]
            t = sensor_i - sensor_last_i

        else: # if array has looped around
            new_accels = vstack(              # concatenate...
                    accel[:, sensor_last_i:], # last to end and ...
                    accel[:, :sensor_i])      # begininning to current
            t = sensor_frames_stored + sensor_i - sensor_last_i

        # calculate next velocity:
        # v2 = v1 + a1*t1+a2*t2+...
        v = v_old + np.sum(new_accels, axis = 2)*accel_time_step # sum along each dimension

        # calculate next 
        # d = v_avg*dt
        d = (v_old + v)/2*t*dt

        # transform by angles - heading and pitch
        pitch = gyro[gyro_pitch_axis,sensor_i]
        heading_old = heading;
        heading = np.arctan(np.true_divide(mag[0,sensor_i],mag[1,sensor_i])) - zero_angle
        #d = # TODO - figure out x-y-z
        heading_curr = (heading-heading_old)/2
        dx = d*np.cos(heading_curr)*np.cos(pitch)
        dy = d*np.sin(heading_curr)*np.cos(pitch)


        # increment index
        #xy_i = (xy_i + 1) % xy_frames_stored

        return dx[xy_i],dy[xy_i],heading[sensor_i], self.confirm_distance()


    def confirm_distance(self):
        return 1 # for now

        # new way:
        # cumulatively sum distances since last encoder reading
        # when encoder is read - compare to accel distance
        # if too far off - skipping
        # otherwise - correct? maybe (imperfect because doesn't account for all directional stuff
        # TODO: how to deal with turns???

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
