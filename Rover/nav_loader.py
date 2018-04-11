from navSystem_hall import navsystem
global nav
nav = navsystem(
        xy_frames_stored = 5,
        sensor_frames_stored = 20,
        encoder_frames_stored = 20,
        zero_angle = 0, # TODO modify this to run parallel to rows of field
        encoder_distance = 2.7474,
        skid_err_range = .5, # TODO adjust based on tests
        accel_time_step = .05,# TODO set before running
        gyro_pitch_axis = 1, # Y/1 for PCB
        )
print(nav)
