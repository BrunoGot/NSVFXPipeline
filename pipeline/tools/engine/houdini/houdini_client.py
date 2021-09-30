import threading
import socket
import time
import hou


class Client(threading.Thread):
    def __init__(self):
        self.active_client = True
        threading.Thread.__init__(self)
        self.msgClient = "Hello Server"
        self.msgToSend = str.encode(self.msgClient)
        self.addrPort = ("127.0.0.1", 9999)
        self.bufferSize = 1024

        # Creer un socket udp cote client
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.connect(self.addrPort)
        print("Client started")
        self.create_midi_mapper_chop()

        #dico that containing assignation
        self.assignations = {} #{channel_name, midi_slot_parm} the midi signal control the midi slot, wich is trigging the final parm destination

    def run(self):
        i = 0
        while (self.active_client):
            self.send_msg()
            msg = self.receiv_msg()
            self.compute_datas(msg)
        self.socket.close()
        print("client quit")

    def send_msg(self):
        # envoyer le msg
        self.socket.sendto(self.msgToSend, self.addrPort)
        print("send msg " + self.msgToSend)

    def receiv_msg(self):
        msgServer = self.socket.recvfrom(self.bufferSize)
        msg = "Message du serveur {}".format(msgServer[0])
        print(msg)
        return msgServer[0]

    def compute_datas(self, datas):
        print("datas = " + datas)
        if datas == "Create":
            hou.node("/obj").createNode("geo")
        elif datas == "Quit":
            self.active_client=False
        elif "Context" in datas:
            pack = datas.split(',')
            pane = hou.ui.paneTabOfType(hou.paneTabType.NetworkEditor)
            if pane:  # if the panel is valid
                path = pane.pwd().path()
                print(str(pack))
                if pack[1]=="1": #1 : obj context
                    path = "/obj"
                elif pack[1]=="2": #img context
                    path = "/img"
                elif pack[1]=="3": #img context
                    path = "/mat"
                pane.cd(path) #change the context here
                #pane.redraw()

        elif "," in datas:
            pack = datas.split(',') #slot,target, value
            name = pack[0]
            adress = pack[1]
            value = float(pack[2])
            if "New" in datas:
                print("create new slider")
                self.set_new_assignation(name, adress, value)
            if name in self.assignations:
                value = value/127 #normalize to be between 0 -1
                slot_path = self.assignations[name] #get the corresponding midi_slot to control it
                """if(parm.expression()):
                    print(parm.expression())"""
                hou.node(".").parm(slot_path).set(value)

    def count(self):
        i = 0
        while (i < 10):
            time.sleep(0.5)
            i += 1
        client.active_client = False

    def create_midi_mapper_chop(self):
        """create a chop node to handle mapping signals"""
        self.midi_handler = hou.node("ch/").createNode("ch", "midi_handler")
        self.midi_mapper = self.midi_handler.createNode("null", "midi_mapper")
        self.parmgroup = self.midi_mapper.parmTemplateGroup()

    def set_new_assignation(self, channel_id, adress, value):
        if(hou.node(".").parm(adress)): #check if the adress is valid
            midi_slot = self.add_midi_slot(channel_id, value)
            slot_path = self.midi_mapper.path()+"/"+midi_slot.name() #path to the midi slot
            self.assignations[channel_id] = slot_path
            print("assign to "+self.midi_mapper.path()+"/"+midi_slot.name())
            hou.node(".").parm(adress).setExpression("ch('{0}')".format(slot_path))

    def add_midi_slot(self, channel_id, val):
        """add midi slot to the midi mapping node"""
        name = "ch"+str(channel_id)
        print("val = "+str(val))
        slider = hou.FloatParmTemplate(name,name,1)
        self.parmgroup.append(slider)
        self.midi_mapper.setParmTemplateGroup(self.parmgroup)
        return slider

if __name__ == "__main__":
    client = Client()
    client.start()
    # client.count()
