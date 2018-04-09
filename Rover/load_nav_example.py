from navSystem_hall import navsystem
nav = navsystem(
        xy_frames_stored = 5,
        sensor_frames_stored = 20,
        encoder_frames_stored = 20,
        zero_angle = 0,
        encoder_distance = 2.7474,
        skid_err_range = .5,
        accel_time_step = 0.05,
        gyro_pitch_axis = 1,)
