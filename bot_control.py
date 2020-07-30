from direct.task import Task
from math import pi, sin, cos
from panda3d.core import MouseButton
from direct.showbase.ShowBase import ShowBase


class App(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)
        self.positions = {
            "drone": (0, 5, -0.7),
            "mp": (0.5, 5, -1),
            "camera": (0, 0, 0)
        }
        self.left = True
        self.wasClicked = False
        #Main scene
        self.scene = self.loader.loadModel("models/environment.dae")
        self.scene.reparentTo(self.render)
        self.scene.setScale(0.5, 0.5, 0.5)
        self.scene.setPos(1, 10, -1)
        self.scene.setH(self.scene, 90)
        self.scene.setP(self.scene, 90)
        self.scene.setR(self.scene, -5)
        rt = self.loader.loadTexture("models/Racks.png")
        self.scene.setTexture(rt, 0)
        #Drone
        self.drone = self.loader.loadModel("models/drone.dae")
        self.drone.reparentTo(self.render)
        self.drone.setPos(*self.positions["drone"])
        dt = self.loader.loadTexture("models/Drone.png")
        self.drone.setTexture(dt, 0)
        self.drone.setScale(2, 2, 2)
        self.drone.setH(self.drone, 90) 
        self.drone.setP(self.drone, 90)
        #Mobile Platform
        self.mp = self.loader.loadModel("models/mp.dae")
        mpt = self.loader.loadTexture("models/MP.png")
        self.mp.setTexture(mpt, 0)
        self.mp.setH(self.mp, -90)
        self.mp.setP(self.mp, 90)
        self.mp.reparentTo(self.render)
        self.mp.setPos(*self.positions["mp"])
        self.mp.setScale(0.15, 0.15, 0.15)
        base.disableMouse()
        #Camera setups 
        self.taskMgr.add(self.updateStateTask, "updateStateTask")
        self.accept("w", self.keyHandler, ["w"])
        self.accept("s", self.keyHandler, ["s"])
        self.accept("a", self.keyHandler, ["a"])
        self.accept("d", self.keyHandler, ["d"])
        self.accept("f", self.keyHandler, ["f"])



    def keyHandler(self, key):
        if(key == "w"):
            X, Y, Z = self.positions["mp"]
            new_position = (X, Y+0.05, Z)
            self.positions["mp"] = new_position
            self.mp.setPos(*new_position)
            X, Y, Z = self.positions["drone"]
            new_position = (X, Y+0.05, Z)
            self.positions["drone"] = new_position
            self.drone.setPos(*new_position)
            X, Y, Z = self.positions["camera"]
            new_position = (X, Y+0.05, Z)
            self.positions["camera"] = new_position
            self.camera.setPos(*new_position)
        elif(key == "s"):
            X, Y, Z = self.positions["mp"]
            new_position = (X, Y-0.05, Z)
            self.positions["mp"] = new_position
            self.mp.setPos(*new_position)
            X, Y, Z = self.positions["drone"]
            new_position = (X, Y-0.05, Z)
            self.positions["drone"] = new_position
            self.drone.setPos(*new_position)
            X, Y, Z = self.positions["camera"]
            new_position = (X, Y-0.05, Z)
            self.positions["camera"] = new_position
            self.camera.setPos(*new_position)
        elif(key == "a"):
            X, Y, Z = self.positions["mp"]
            new_position = (X-0.05, Y, Z)
            self.positions["mp"] = new_position
            self.mp.setPos(*new_position)
            X, Y, Z = self.positions["drone"]
            new_position = (X-0.05, Y, Z)
            self.positions["drone"] = new_position
            self.drone.setPos(*new_position)
            X, Y, Z = self.positions["camera"]
            new_position = (X-0.05, Y, Z)
            self.positions["camera"] = new_position
            self.camera.setPos(*new_position)
        elif(key == "d"):
            X, Y, Z = self.positions["mp"]
            new_position = (X+0.05, Y, Z)
            self.positions["mp"] = new_position
            self.mp.setPos(*new_position)
            X, Y, Z = self.positions["drone"]
            new_position = (X+0.05, Y, Z)
            self.positions["drone"] = new_position
            self.drone.setPos(*new_position)
            X, Y, Z = self.positions["camera"]
            new_position = (X+0.05, Y, Z)
            self.positions["camera"] = new_position
            self.camera.setPos(*new_position)
        elif(key == "f"):
            X, Y, Z = self.positions["drone"]
            new_position = (X+1 if self.left else X-1, Y, Z)
            self.left = not self.left
            self.positions["drone"] = new_position
            self.drone.setPos(*new_position)
            
            




    # Define a procedure to move the camera.
    def updateStateTask(self, task):
        if base.mouseWatcherNode.hasMouse():
            if base.mouseWatcherNode.isButtonDown(MouseButton.three()):
                if not self.wasClicked:
                    self.wasClicked = True
            else:
                if self.wasClicked:
                    self.wasClicked = False
                    X, Y, Z = self.positions["drone"]
                    new_position = (X, Y, Z+0.05)
                    self.positions["drone"] = new_position
                    self.drone.setPos(*new_position)
            if base.mouseWatcherNode.isButtonDown(MouseButton.one()):
                if not self.wasClicked:
                    self.wasClicked = True
            else:
                if self.wasClicked:
                    self.wasClicked = False
                    X, Y, Z = self.positions["drone"]
                    new_position = (X, Y, Z-0.05)
                    self.positions["drone"] = new_position
                    self.drone.setPos(*new_position)

        return Task.cont


app = App()
app.run()
