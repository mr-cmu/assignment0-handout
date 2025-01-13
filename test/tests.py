import numpy as np
import sys

sys.path.append('../')

from quadrotor_simulator_py.utils import Pose
from quadrotor_simulator_py.utils import Quaternion
from quadrotor_simulator_py.utils import Rot3
from quadrotor_simulator_py.utils import transforms

eps = 1e-2
R1 = np.array([[ 0.8253, -0.412 , -0.3862],
               [ 0.0083,  0.6926, -0.7213],
               [ 0.5646,  0.5921,  0.575 ]])
rpy1 = [ 0.8, -0.6,  0.01]
q1 = np.array([0.8793, 0.3734, -0.2703, 0.1195])

R2 = np.array([[0.9999,   -0.0109,   -0.0090],
               [0.0100,    0.9949,   -0.0999],
               [0.0100,    0.0998,    0.9950]])
rpy2 = np.array([ 0.1, -0.01,  0.01])
q2 = np.array([0.9987, 0.0500, -0.0047, 0.0052])

R3 = np.array([[ 0.1691,    0.3851,   -0.9072],
               [-0.0170,    0.9215,    0.3880],
               [ 0.9854,   -0.0502,    0.1624]])
rpy3 = np.array([ -0.3, -1.4,  -0.1])
q3 = np.array([0.7505, -0.1460, -0.6305, -0.1339])

R4 = np.array([[-0.0858,   -0.6806,    0.7276],
               [-0.1467,   -0.7137,   -0.6849],
               [ 0.9854,   -0.1655,   -0.0386]])
rpy4 = np.array([ -1.8, -1.4,  -2.1])
q4 = np.array([-0.2012, -0.6455, 0.3204, -0.6635])

def check_soln(student_soln, correct_soln):
    score = 0.
    try:
        if np.linalg.norm(student_soln-correct_soln) < eps:
            score += 0.25
            print('passed')
        else:
            print('failed')
    except Exception as e:
            print('failed')

    return score

def test_to_euler_zyx():
    score = 0.
    print(f"to_euler_zyx test 1...", end="")
    r = R1
    student_soln = Rot3(r).to_euler_zyx()
    correct_soln = np.array(rpy1)
    score+=check_soln(student_soln,correct_soln)

    print(f"to_euler_zyx test 2...", end="")
    r = R2
    student_soln = Rot3(r).to_euler_zyx()
    correct_soln = rpy2
    score+=check_soln(student_soln,correct_soln)

    print(f"to_euler_zyx test 3...", end="")
    r = R3
    student_soln = Rot3(r).to_euler_zyx()
    correct_soln = rpy3
    score+=check_soln(student_soln,correct_soln)

    print(f"to_euler_zyx test 4...", end="")
    r = R4
    student_soln = Rot3(r).to_euler_zyx()
    correct_soln = rpy4
    score+=check_soln(student_soln,correct_soln)
    return score


def test_from_euler_zyx():
    score = 0.
    print(f"from_euler_zyx test 1...", end="")
    r = rpy1
    student_soln = Rot3().from_euler_zyx(r).R
    correct_soln = R1
    score+=check_soln(student_soln,correct_soln)
 
    print(f"from_euler_zyx test 2...", end="")
    r = rpy2
    student_soln = Rot3().from_euler_zyx(r).R
    correct_soln = R2
    score+=check_soln(student_soln,correct_soln)

    print(f"from_euler_zyx test 3...", end="")
    r = rpy3
    student_soln = Rot3().from_euler_zyx(r).R
    correct_soln = R3
    score+=check_soln(student_soln,correct_soln)

    print(f"from_euler_zyx test 4...", end="")
    r = rpy4
    student_soln = Rot3().from_euler_zyx(r).R
    correct_soln = R4
    score+=check_soln(student_soln,correct_soln)
    return score

def test_roll():
    score = 0.
    print(f"roll test 1...", end="")
    R = R1
    student_soln = np.array([Rot3(R).roll()])
    correct_soln = np.array([rpy1[0]])
    score+=check_soln(student_soln,correct_soln)

    print(f"roll test 2...", end="")
    R = R2
    student_soln = np.array([Rot3(R).roll()])
    correct_soln = np.array(rpy2[0])
    score+=check_soln(student_soln,correct_soln)

    print(f"roll test 3...", end="")
    R = R3
    student_soln = np.array([Rot3(R).roll()])
    correct_soln = np.array(rpy3[0])
    score+=check_soln(student_soln,correct_soln)

    print(f"roll test 4...", end="")
    R = R4
    student_soln = np.array([Rot3(R).roll()])
    correct_soln = np.array(rpy4[0])
    score+=check_soln(student_soln,correct_soln)

    return score

def test_pitch():
    score = 0.
    print(f"pitch test 1...", end="")
    R = R1
    student_soln = np.array([Rot3(R).pitch()])
    correct_soln = np.array([rpy1[1]])
    score+=check_soln(student_soln,correct_soln)

    print(f"pitch test 2...", end="")
    R = R2
    student_soln = np.array([Rot3(R).pitch()])
    correct_soln = np.array(rpy2[1])
    score+=check_soln(student_soln,correct_soln)

    print(f"pitch test 3...", end="")
    R = R3
    student_soln = np.array([Rot3(R).pitch()])
    correct_soln = np.array(rpy3[1])
    score+=check_soln(student_soln,correct_soln)

    print(f"pitch test 4...", end="")
    R = R4
    student_soln = np.array([Rot3(R).pitch()])
    correct_soln = np.array(rpy4[1])
    score+=check_soln(student_soln,correct_soln)
    return score

def test_yaw():
    score = 0.
    print(f"yaw test 1...", end="")
    R = R1
    student_soln = np.array([Rot3(R).yaw()])
    correct_soln = np.array([rpy1[2]])
    score+=check_soln(student_soln,correct_soln)

    print(f"yaw test 2...", end="")
    R = R2
    student_soln = np.array([Rot3(R).yaw()])
    correct_soln = np.array(rpy2[2])
    score+=check_soln(student_soln,correct_soln)

    print(f"yaw test 3...", end="")
    R = R3
    student_soln = np.array([Rot3(R).yaw()])
    correct_soln = np.array(rpy3[2])
    score+=check_soln(student_soln,correct_soln)

    print(f"yaw test 4...", end="")
    R = R4
    student_soln = np.array([Rot3(R).yaw()])
    correct_soln = np.array(rpy4[2])
    score+=check_soln(student_soln,correct_soln)
    return score

def test_to_quat():
    score = 0.
    print(f"quat test 1...", end="")
    R = R1
    student_soln = np.array(Rot3(R).to_quat().data)
    correct_soln = Quaternion(q1).data
    score+=check_soln(student_soln,correct_soln)

    print(f"quat test 2...", end="")
    R = R2
    student_soln = np.array([Rot3(R).to_quat().data])
    correct_soln = Quaternion(q2).data
    score+=check_soln(student_soln,correct_soln)

    print(f"quat test 3...", end="")
    R = R3
    student_soln = np.array([Rot3(R).to_quat().data])
    correct_soln = Quaternion(q3).data
    score+=check_soln(student_soln,correct_soln)

    print(f"quat test 4...", end="")
    R = R4
    student_soln = np.array([Rot3(R).to_quat().data])
    correct_soln = Quaternion(q4).data
    score+=check_soln(student_soln,correct_soln)
    return score

def test_from_quat():
    score = 0.
    print(f"quat test 1...", end="")
    R = R1
    correct_soln = R
    student_soln = Rot3().from_quat(Quaternion(q1)).R
    score+=check_soln(student_soln,correct_soln)

    print(f"quat test 2...", end="")
    R = R2
    correct_soln = R
    student_soln = Rot3().from_quat(Quaternion(q2)).R
    score+=check_soln(student_soln,correct_soln)

    print(f"quat test 3...", end="")
    R = R3
    correct_soln = R
    student_soln = Rot3().from_quat(Quaternion(q3)).R
    score+=check_soln(student_soln,correct_soln)

    print(f"quat test 4...", end="")
    R = R4
    correct_soln = R
    student_soln = Rot3().from_quat(Quaternion(q4)).R
    score+=check_soln(student_soln,correct_soln)
    return score

def test_pose_compose():
    print(f"pose compose test...", end="")
    score = 0.
    t1 = np.array([1., 2., 3.])
    data = np.append(t1, q1).T
    pose = Pose(data)

    t2 = np.array([0, 2., 0])

    studentT = pose.compose(Pose(np.append(t2, q2).T))
    correctT = np.array([[ 0.8173114 , -0.45746179 ,-0.35032953  ,0.17592375],
                        [ 0.0080136 ,  0.61696969 ,-0.78694611  ,3.38513088],
                        [ 0.57614048,  0.64037263 , 0.50792228  ,4.18419204],
                        [ 0.        ,  0.         , 0.          ,1.        ]])
    score+=check_soln(studentT.get_se3(),correctT)*4
    return score
    
def test_pose_inverse():
    print(f"pose inverse test...", end="")
    score = 0.
    t1 = np.array([1., 2., 3.])
    data = np.append(t1, q1).T
    pose = Pose(data)
    studentT = pose.inverse()
    correctT = np.array([[ 0.82530456,  0.00829317,  0.56462697, -2.5357718 ],
                         [-0.41203813,  0.69256544,  0.59209602, -2.74938081],
                         [-0.38613077, -0.72130738,  0.57499452,  0.10376198],
                         [ 0.        ,  0.        ,  0.        ,  1.        ]])
    score+=check_soln(studentT.get_se3(),correctT)*4
    return score

def test_transforms():
    print(f"transforms test...", end="")
    score = 0.
    studentT = transforms.set_robot_transforms()
    correctT = np.array([[-2.91995223e-02, -2.91870717e-02,  9.99147388e-01,  4.15000000e+00],
                         [-9.99573603e-01,  8.52612103e-04, -2.91870717e-02,  1.00000000e+00],
                         [-5.55111512e-17, -9.99573603e-01, -2.91995223e-02,  2.94000000e+00],
                         [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  1.00000000e+00]])
    score+=check_soln(studentT.get_se3(),correctT)*4
    return score

if __name__ == "__main__":
    test_to_euler_zyx()
    test_from_euler_zyx()
    test_roll()
    test_pitch()
    test_yaw()
    test_to_quat()
    test_from_quat()
    test_pose_compose()
    test_pose_inverse()
    test_transforms()
