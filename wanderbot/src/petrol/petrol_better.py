#!/usr/bin/env python
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import math

waypoints = [
    [(2.1, 2.2, 0.0), (0.0, 0.0, 0.0, 1.0)],
    [(6.5, 4.43, 0.0), (0.0, 0.0, -0.984047240305, 0.177907360295)],
    [(3.1, 3.33, 0.0), (0.0, 0.0, -0.4556, 0.134)],
    [(4.1, 4.4, 0.0),(0.0, 0.0, 0.0, 1.0)],
    [(1.0, 2.3, 0.0),(0.0, 0.0, 0.0, 2.0)]
]
def new_pose(p0):
    l_d=1200000
    p_i=p0
    if len(wp1)==0:
        wp1.remove(wp[0])
        return wp[0]
    for p1 in wp1:
        distance=math.sqrt( (p0[0][0]-p1[0][0])**2 + (p0[0][1]-p1[0][1])**2 )
        if distance<=l_d:
            l_d=distance
            p_i=p1
        else:
            l_d=l_d
    wp1.remove(p_i)
    return p_i


def goal_pose(pose):
    goal_pose = MoveBaseGoal()
    goal_pose.target_pose.header.frame_id = 'map'
    goal_pose.target_pose.pose.position.x = pose[0][0]
    goal_pose.target_pose.pose.position.y = pose[0][1]
    goal_pose.target_pose.pose.position.z = pose[0][2]
    goal_pose.target_pose.pose.orientation.x = pose[1][0]
    goal_pose.target_pose.pose.orientation.y = pose[1][1]
    goal_pose.target_pose.pose.orientation.z = pose[1][2]
    goal_pose.target_pose.pose.orientation.w = pose[1][3]
    return goal_pose

if __name__ == '__main__':
    rospy.init_node('patrol')
    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    client.wait_for_server()
    wp1=waypoints
    pose=wp1[0]
    while len(wp1)!=0:
        pose=new_pose(pose)
        goal = goal_pose(pose)
        client.send_goal(goal)
        client.wait_for_result()
        
