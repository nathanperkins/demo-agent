FROM ros:melodic-robot-bionic

ENV IM_IN_DOCKER Yes
ENV ROS_MASTER_URI=http://localhost:11311

# Add demo_agent package and run catkin_make
RUN mkdir -p /catkin_ws/src/demo_agent
COPY . /catkin_ws/src/demo_agent
RUN /bin/bash -c "source /opt/ros/melodic/setup.bash; cd catkin_ws; catkin_make"

RUN apt update
RUN /bin/bash -c "source /catkin_ws/devel/setup.bash; cd catkin_ws/src/demo_agent; rosdep install --from-paths . -v -y"

CMD ["/catkin_ws/src/demo_agent/start.sh"]
