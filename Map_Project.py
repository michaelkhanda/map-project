print("Hello World")
from tkinter import *
import operator

# Create object
root = Tk()

# Adjust size
root.geometry("400x400")
root['bg'] = '#ffbf00'

# datatype of menu text
clicked = StringVar()
clicked1 = StringVar()


class mappy():
    Walk = {"Gate A": set(["Procurement", "Administration Block", "Administration Parking"]),
            "Administration Block": set(["Lillian K Beam", "Gate A", "Administration Parking", "Mama Africa", "Transport Office"]),
            "Administration Parking": set(["Gate A", "Transport Office"]),
            "Main Lab": set(["Old Humanities", "Mama Africa", "Lillian K Beam", "Cafeteria", "Wooden Blocks", "Hostels","Basketball Court", "Library", "Procurement", "Auditorium"]),
            "Procurement": set(["Wooden Blocks", "Mama Africa", "Gate A", "Main Lab"]),
            "Mama Africa": set(["Lillian K Beam", "Wooden Blocks", "Procurement", "Administration Block", "Main Lab"]),
            "Wooden Blocks": set(["Main Lab", "Procurement", "Cafeteria", "Mama Africa", "Old Humanities"]),
            "Lillian K Beam": set(["Cafeteria", "Administration Block", "Main Lab"]),
            "Cafeteria": set(["Lillian K Beam", "Cafeteria Outdoors Sitting Area", "Wooden Blocks", "Main Lab", "Hostels", "Library","Auditorium", "School of Business", "Old Humanities", "Transport Office"]),
            "Cafeteria Outdoors Sitting Area": set(["Cafeteria"]),
            "Old Humanities": set(["Wooden Blocks", "School of Business", "Main Lab", "Auditorium", "Library", "Cafeteria", "Hostels","Basketball Court"]),
            "School of Business": set(["Old Humanities", "Main Lab", "Auditorium", "Library", "Cafeteria", "Hostels", "Basketball Court"]),
            "Hostels": set(["Cafeteria", "Cafe Latta", "School of Business", "Auditorium", "Library", "Old Humanities", "Main Lab","Transport Office", "Basketball Court"]),
            "Hostels Cafe Latta & Cyber Cafe": set(["Cafe Latta", "Auditorium", "Library", "Basketball Court"]),
            "Transport Office": set(["Cafe Latta", "Hostels", "Administration Parking", "Cafeteria", "Administration Block","Cafe Latta Parking Lot"]),
            "Cafe Latta": set(["Cafe Latta Parking Lot", "Hostels", "Transport Office", "Bus Parking Lot","Hostels Cafe Latta & Cyber Cafe"]),
            "Cafe Latta Parking Lot": set(["Bus Parking Lot", "Cafe Latta", "Faculty Housing", "Student Centre Parking Lot", "Hostels","Transport Office"]),
            "Basketball Court": set(["Hostels Cafe Latta & Cyber Cafe", "Bus Parking Lot", "Auditorium", "Library", "School of Business","Old Humanities", "Cafeteria", "Student Centre Parking Lot", "Student Centre"]),
            "Auditorium": set(["Basketball Court", "Library", "Auditorium Parking", "Student Centre Parking Lot", "Student Centre","School of Business", "Old Humanities", "Cafeteria", "Main Lab", "Hostels Cafe Latta & Cyber Cafe","Hostels"]),
            "Auditorium Parking": set(["Auditorium", "Student Centre Parking Lot", "Student Centre"]),
            "Bus Parking Lot": set(["Basketball Court", "Hostels Cafe Latta & Cyber Cafe", "Cafe Latta Parking Lot","Student Centre Parking Lot", "Student Centre", "Faculty Housing"]),
            "Faculty Housing": set(["Cafe Latta Parking Lot", "Bus Parking Lot", "Student Centre Parking Lot"]),
            "Library": set(["Auditorium", "School of Business", "Old Humanities", "Cafeteria", "Main Lab", "Library Parking","School of Science", "School of Science Parking"]),
            "Library Parking": set(["Library", "School of Science Parking"]),
            "Student Centre Parking Lot": set(["Faculty Housing", "Auditorium Parking", "Auditorium", "Student Centre", "Basketball Court"]),
            "Student Centre": set(["School of Science", "Student Centre Parking Lot", "Swimming Pool Parking", "Auditorium","Basketball Court"]),
            "School of Science": set(["New Humanities", "Swimming Pool Parking", "School of Science Parking"]),
            "School of Science Parking": set(["School of Science", "Swimming Pool Parking", "Library", "Library Parking"]),
            "Swimming Pool Parking": set(["Swimming Pool", "New Humanities", "School of Science"]),
            "Swimming Pool": set(["Swimming Pool Parking"]),
            "New Humanities": set(["School of Science", "School of Humanities Parking Lot", "Gate B", "Football Pitch"]),
            "School of Humanities Parking Lot": set(["Gate B", "New Humanities"]),
            "Gate B": set(["New Humanities", "School of Humanities Parking Lot"]),
            "Football Pitch": set(["New Humanities", "Rugby Field"]),
            "Rugby Field": set(["Football Pitch"])

            }

    Drive = {"Gate A": set(["Administration Parking"]),
             "Administration Parking": set(["Gate A", "Cafe Latta Parking Lot", "Bus Parking Lot"]),
             "Cafe Latta Parking Lot": set(["Administration Parking", "Bus Parking Lot", "Student Centre Parking", "Auditorium Parking"]),
             "Bus Parking Lot": set(["Administration Parking", "Cafe Latta Parking Lot", "Student Centre Parking", "Auditorium Parking"]),
             "Student Centre Parking": set(["Cafe Latta Parking Lot", "Bus Parking Lot", "Auditorium Parking", "Swimming Pool Parking"]),
             "Auditorium Parking": set(["Cafe Latta Parking Lot", "Bus Parking Lot", "Student Centre Parking", "Swimming Pool Parking"]),
             "Swimming Pool Parking": set(["Auditorium Parking", "Student Centre Parking", "School of Humanities Parking Lot","School of Science Parking"]),
             "School of Science Parking": set(["Library Parking", "Swimming Pool Parking"]),
             "Library Parking": set(["School of Science Parking"]),
             "School of Humanities Parking Lot": set(["Swimming Pool Parking", "Gate B"]),
             "Gate B": set(["School of Humanities Parking Lot"])

             }


    WalkCost = {str(["Gate A", "Procurement"]): "145",
                str(["Gate A", "Administration Block"]): "105",
                str(["Gate A", "Administration Parking"]): "95",

                str(["Administration Block", "Lillian K Beam"]): "20",
                str(["Administration Block", "Gate A"]): "105",
                str(["Administration Block", "Administration Parking"]): "15",
                str(["Administration Block", "Mama Africa"]): "15",
                str(["Administration Block", "Transport Office"]): "55",

                str(["Administration Parking", "Gate A"]): "95",
                str(["Administration Parking", "Transport Office"]): "45",
                str(["Administration Parking", "Administration Block"]): "2",

                str(["Main Lab", "Old Humanities"]): "45",
                str(["Main Lab", "Mama Africa"]): "30",
                str(["Main Lab", "Lillian K Beam"]): "50",
                str(["Main Lab", "Cafeteria"]): "29",
                str(["Main Lab", "Wooden Blocks"]): "37",
                str(["Main Lab", "Hostels"]): "150",
                str(["Main Lab", "Basketball Court"]): "195",
                str(["Main Lab", "Library"]): "250",
                str(["Main Lab", "Procurement"]): "50", 
                str(["Main Lab", "Auditorium"]): "205",
                str(["Main Lab", "School of Business"]): "57",

                str(["Procurement", "Wooden Blocks"]): "20",  
                str(["Procurement", "Mama Africa"]): "50",   
                str(["Procurement", "Gate A"]): "145",   
                str(["Procurement", "Main Lab"]): "50",   

                str(["Mama Africa", "Lillian K Beam"]): "30",
                str(["Mama Africa", "Wooden Blocks"]): "56",
                str(["Mama Africa", "Procurement"]): "50",   
                str(["Mama Africa", "Administration Block"]): "9",
                str(["Mama Africa", "Main Lab"]): "30",

                str(["Wooden Blocks", "Main Lab"]): "37",
                str(["Wooden Blocks", "Procurement"]): "20",   
                str(["Wooden Blocks", "Cafeteria"]): "40",
                str(["Wooden Blocks", "Mama Africa"]): "50",
                str(["Wooden Blocks", "Old Humanities"]): "15",

                str(["Lillian K Beam", "Cafeteria"]): "30",
                str(["Lillian K Beam", "Administration Block"]): "25",
                str(["Lillian K Beam", "Main Lab"]): "50",
                str(["Lillian K Beam", "Mama Africa"]): "50",

                str(["Cafeteria", "Lillian K Beam"]): "30",
                str(["Cafeteria", "Wooden Blocks"]): "40",
                str(["Cafeteria", "Main Lab"]): "29",
                str(["Cafeteria", "Hostels"]): "44",
                str(["Cafeteria", "Library"]): "120",
                str(["Cafeteria", "Auditorium"]): "105",
                str(["Cafeteria", "School of Business"]): "121",
                str(["Cafeteria", "Old Humanities"]): "141",
                str(["Cafeteria", "Transport Office"]): "21",
                str(["Cafeteria", "Basketball Court"]): "73",
                str(["Cafeteria", "Cafeteria Outdoors Sitting Area"]): "5",

                str(["Cafeteria Outdoors Sitting Area", "Cafeteria"]): "5",

                str(["Old Humanities", "Wooden Blocks"]): "19",
                str(["Old Humanities", "School of Business"]): "27",
                str(["Old Humanities", "Main Lab"]): "17",
                str(["Old Humanities", "Auditorium"]): "118",
                str(["Old Humanities", "Library"]): "105",
                str(["Old Humanities", "Cafeteria"]): "141",
                str(["Old Humanities", "Hostels"]): "127",
                str(["Old Humanities", "Basketball Court"]): "150",

                str(["School of Business", "Old Humanities"]): "27",
                str(["School of Business", "Main Lab"]): "59",
                str(["School of Business", "Auditorium"]): "39",
                str(["School of Business", "Library"]): "52",
                str(["School of Business", "Cafeteria"]): "121",
                str(["School of Business", "Hostels"]): "131",
                str(["School of Business", "Basketball Court"]): "167",

                str(["Hostels", "Cafeteria"]): "44",
                str(["Hostels", "Cafe Latta"]): "5",
                str(["Hostels", "School of Business"]): "131",
                str(["Hostels", "Auditorium"]): "75",
                str(["Hostels", "Library"]): "120",
                str(["Hostels", "Old Humanities"]): "127",
                str(["Hostels", "Main Lab"]): "150",
                str(["Hostels", "Transport Office"]): "10",
                str(["Hostels", "Basketball Court"]): "70",

                str(["Cyber Cafe", "Cafe Latta"]): "2",
                str(["Cyber Cafe", "Auditorium"]): "80",
                str(["Cyber Cafe", "Library"]): "115",
                str(["Cyber Cafe", "Basketball Court"]): "90",
                str(["Cyber Cafe", "Bus Parking Lot"]): "20",

                str(["Transport Office", "Cafe Latta"]): "13",
                str(["Transport Office", "Hostels"]): "10",
                str(["Transport Office", "Administration Parking"]): "15",
                str(["Transport Office", "Cafeteria"]): "15",
                str(["Transport Office", "Administration Block"]): "35",
                str(["Transport Office", "Cafe Latta Parking Lot"]): "30",

                str(["Cafe Latta", "Cafe Latta Parking Lot"]): "5",
                str(["Cafe Latta", "Hostels"]): "5",
                str(["Cafe Latta", "Hostels Caffe Latta & Cyber Cafe"]): "10",
                str(["Cafe Latta", "Transport Office"]): "13",
                str(["Cafe Latta", "Bus Parking Lot"]): "21",
                str(["Cafe Latta", "Cyber Cafe"]): "2",

                str(["Hostels Caffe Latta & Cyber Cafe", "Cafe Latta"]): "10",

                str(["Cafe Latta Parking Lot", "Bus Parking Lot"]): "4",
                str(["Cafe Latta Parking Lot", "Cafe Latta"]): "2",
                str(["Cafe Latta Parking Lot", "Faculty Housing"]): "15",
                str(["Cafe Latta Parking Lot", "Student Centre Parking"]): "105",
                str(["Cafe Latta Parking Lot", "Hostels"]): "10",
                str(["Cafe Latta Parking Lot", "Transport Office"]): "30",

                str(["Basketball Court", "Cyber Cafe"]): "90",
                str(["Basketball Court", "Bus Parking Lot"]): "25",
                str(["Basketball Court", "Auditorium"]): "11",
                str(["Basketball Court", "Library"]): "107",
                str(["Basketball Court", "School of Business"]): "155",
                str(["Basketball Court", "Old Humanities"]): "150",
                str(["Basketball Court", "Cafeteria"]): "125",
                str(["Basketball Court", "Student Centre Parking"]): "35",
                str(["Basketball Court", "Student Centre"]): "115",
                str(["Basketball Court", "Main Lab"]): "133",
                str(["Basketball Court", "Hostels"]): "35",

                str(["Auditorium", "Basketball Court"]): "11",
                str(["Auditorium", "Library"]): "65",
                str(["Auditorium", "Auditorium Parking"]): "5",
                str(["Auditorium", "Student Centre Parking"]): "45",
                str(["Auditorium", "Student Centre"]): "125",
                str(["Auditorium", "School of Business"]): "75",
                str(["Auditorium", "Old Humanities"]): "118",
                str(["Auditorium", "Cafeteria"]): "105",
                str(["Auditorium", "Main Lab"]): "205",
                str(["Auditorium", "Cyber Cafe"]): "80",
                str(["Auditorium", "Hostels"]): "75",

                str(["Auditorium Parking", "Auditorium"]): "5",
                str(["Auditorium Parking", "Student Centre Parking"]): "35",
                str(["Auditorium Parking", "Student Centre"]): "115",

                str(["Bus Parking Lot", "Basketball Court"]): "25",
                str(["Bus Parking Lot", "Cyber Cafe"]): "70",
                str(["Bus Parking Lot", "Cafe Latta Parking Lot"]): "2",
                str(["Bus Parking Lot", "Student Centre Parking"]): "70",
                str(["Bus Parking Lot", "Student Centre"]): "170",
                str(["Bus Parking Lot", "Faculty Housing"]): "30",

                str(["Faculty Housing", "Cafe Latta Parking Lot"]): "5",
                str(["Faculty Housing", "Bus Parking Lot"]): "10",
                str(["Faculty Housing", "Student Centre Parking"]): "75",

                str(["Library", "Auditorium"]): "65",
                str(["Library", "School of Business"]): "90",
                str(["Library", "Old Humanities"]): "105",
                str(["Library", "Cafeteria"]): "120",
                str(["Library", "Main Lab"]): "250",
                str(["Library", "Library Parking"]): "55",
                str(["Library", "School of Science"]): "225",
                str(["Library", "School of Science Parking"]): "205",
                str(["Library", "Hostels"]): "105",
                str(["Library", "Cyber Cafe"]): "110",

                str(["Library Parking", "Library"]): "65",
                str(["Library Parking", "School of Science Parking"]): "165",

                str(["Student Centre Parking", "Faculty Housing"]): "75",
                str(["Student Centre Parking", "Auditorium Parking"]): "35",
                str(["Student Centre Parking", "Auditorium"]): "45",
                str(["Student Centre Parking", "Student Centre"]): "35",
                str(["Student Centre Parking", "Bus Parking Lot"]): "55",

                str(["Student Centre", "School of Science"]): "81",
                str(["Student Centre", "Student Centre Parking"]): "35",
                str(["Student Centre", "Swimming Pool Parking"]): "45",
                str(["Student Centre", "Auditorium"]): "125",
                str(["Student Centre", "Basketball Court"]): "115",
                str(["Student Centre", "Auditorium Parking"]): "65",
                str(["Student Centre", "Bus Parking Lot"]): "115",

                str(["School of Science", "New Humanities"]): "85",
                str(["School of Science", "Swimming Pool Parking"]): "25",
                str(["School of Science", "School of Science Parking"]): "16",
                str(["School of Science", "Student Centre"]): "75",

                str(["School of Science Parking", "School of Science"]): "16",
                str(["School of Science Parking", "Swimming Pool Parking"]): "25",
                str(["School of Science Parking", "Library"]): "175",
                str(["School of Science Parking", "Library Parking"]): "115",

                str(["Swimming Pool Parking", "Swimming Pool"]): "2",
                str(["Swimming Pool Parking", "New Humanities"]): "90",
                str(["Swimming Pool Parking", "School of Science"]): "50",
                str(["Swimming Pool Parking", "Student Centre"]): "15",
                str(["Swimming Pool Parking", "School of Science Parking"]): "25",
                str(["Swimming Pool", "Swimming Pool Parking"]): "2",

                str(["New Humanities", "School of Science"]): "85",
                str(["New Humanities", "School of Humanities Parking Lot"]): "115",
                str(["New Humanities", "Gate B"]): "145",
                str(["New Humanities", "Football Pitch"]): "225",
                str(["New Humanities", "Swimming Pool Parking"]): "75",

                str(["School of Humanities Parking Lot", "Gate B"]): "25",
                str(["School of Humanities Parking Lot", "New Humanities"]): "115",

                str(["Gate B", "New Humanities"]): "145",
                str(["Gate B", "School of Humanities Parking Lot"]): "25",

                str(["Football Pitch", "New Humanities"]): "225",
                str(["Football Pitch", "Rugby Field"]): "95",

                str(["Rugby Field", "Football Pitch"]): "95"
                }

    DriveCost = {str(["Gate A", "Administration Parking"]): "110",

                str(["Administration Parking", "Gate A Block"]): "110",
                str(["Administration Parking", "Bus Parking Lot"]): "220",
                str(["Administration Parking", "Cafe Latta Parking Lot"]): "230",

                str(["Cafe Latta Parking Lot", "Administration Parking"]): "230",
                str(["Cafe Latta Parking Lot"]): "280",
                str(["Cafe Latta Parking Lot", "Bus Parking Lot"]): "55",
                str(["Cafe Latta Parking Lot", "Student Centre Parking Lot"]): "180",
                str(["Cafe Latta Parking Lot", "Auditorium Parking"]): "150",

                str(["Bus Parking Lot", "Administration Parking"]): "220",
                str(["Bus Parking Lot", "Auditorium Parking"]): "135",
                str(["Bus Parking Lot", "Cafe Latta Parking Lot"]): "55",
                str(["Bus Parking Lot", "Student Centre Parking"]): "170",
                str(["Bus Parking Lot", "Student Centre Parking Lot"]): "145",

                str(["Student Centre Parking Lot", "Cafe Latta Parking Lot"]): "180",
                str(["Student Centre Parking Lot", "Swimming Pool Parking"]): "140",
                str(["Student Centre Parking Lot", "Auditorium Parking"]): "130",
                str(["Student Centre Parking Lot", "Bus Parking Lot"]): "135",

                str(["Auditorium Parking", "Cafe Latta Parking Lot"]): "180",
                str(["Auditorium Parking", "Swimming Pool Parking"]): "150",
                str(["Auditorium Parking", "Student Centre Parking Lot"]): "130",
                str(["Auditorium Parking", "Bus Parking Lot"]): "135",

                str(["Swimming Pool Parking", "School of Humanities Parking Lot"]): "300",
                str(["Swimming Pool Parking", "Auditorium Parking"]): "150",
                str(["Swimming Pool Parking", "Student Centre Parking Lot"]): "140",
                str(["Swimming Pool Parking", "School of Science Parking"]): "130",

                str(["School of Science Parking", "Library Parking"]): "150",
                str(["School of Science Parking", "Swimming Pool Parking"]): "130",

                str(["Library Parking", "School of Science Parking"]): "150",

                str(["School of Humanities Parking Lot", "Swimming Pool Parking"]): "300",
                str(["School of Humanities Parking Lot", "Gate B"]): "75",

                str(["Gate B", "School of Humanities Parking Lot"]): "75",

                }

    

    DriveHeuristic = {"Administration Parking": ["160", "40"],
                        "Cafe Latta Parking Lot": ["74", "134"],
                        "Auditorium Parking": ["130", "224"],
                        "Bus Parking Lot": ["94", "152"],
                        "Student Centre Parking Lot": ["74", "220"],
                        "Library Parking": ["210", "224"],
                        "School of Science Parking": ["164", "284"],
                        "Swimming Pool Parking": ["100", "284"],
                        "School of Humanities Parking Lot": ["204", "394"],
                        }
    WalkingHeuristic = {
        "Gate A": ["205", "4"],
        "Administration Block": ["181", "45"],
        "Administration Parking": ["155", "35"],
        "Lillian K Beam": ["185", "67"],
        "Cafeteria": ["155", "85"],
        "Cafeteria Outdoors Sitting Area": ["165", "77"],
        "Main Lab": ["213", "75"],
        "Procurement": ["235", "75"],
        "Mama Africa": ["198", "45"],
        "Wooden Blocks": ["229", "89"],
        "Old Humanities": ["223", "116"],
        "School of Business": ["215", "143"],
        "Hostels": ["127", "105"],
        "Cyber Cafe": ["109", "139"],
        "Transport Office": ["131", "65"],
        "Cafe Latta": ["197", "129"],
        "Cafe Latta Parking Lot": ["169", "129"],
        "Basketball Court": ["95", "169"],
        "Auditorium": ["135", "187"],
        "Auditorium Parking": ["125", "219"],
        "Bus Parking Lot": ["89", "147"],
        "Faculty Housing": ["57", "169"],
        "Library": ["173", "217"],
        "Library Parking": ["205", "219"],
        "Student Centre Parking Lot": ["69", "215"],
        "Student Centre": ["93", "269"],
        "School of Science": ["165", "305"],
        "School of Science Parking": ["159", "279"],
        "Swimming Pool Parking": ["95", "279"],
        "Swimming Pool": ["95", "315"],
        "New Humanities": ["157", "363"],
        "School of Humanities Parking Lot": ["199", "389"],
        "Gate B": ["279", "395"],
        "Football Pitch": ["255", "650"],
        "Hostels Cafe Latta & Cyber Cafe": ["130", "120"],
        "Rugby Field": ["309", "590"],

    }


class Agent(mappy):

    def getH(vertex, goal):
        v = []
        g = []

        for i in mappy.WalkingHeuristic[vertex]:
            v.append(int(i))
        for i in mappy.WalkingHeuristic[goal]:
            g.append(int(i))

        hue = abs(v[0] - g[0]) + abs(v[1] - g[1])  # one will have x axis and another y axis
        return hue

    def CarH(vertex, goal):
        v = []
        g = []

        for i in mappy.DrivingHeuristic[vertex]:
            v.append(int(i))
        for i in mappy.DrivingHeuristic[goal]:
            v.append(int(i))

        hue = abs(v[0] - g[0]) + abs(v[1] - g[1])  # one will have x axis and another y axis

    def GBFS(graph, start, goal):
        p = []  # host the path
        p.append(start)

        while True:  # creating an infinite loop
            neighbour = graph[start]
            h = {}

            for i in neighbour.difference(p):  # go to all neighbours except those we have visited
                h[i] = Agent.getH(i, goal)  # needs this info to calculate heuristics

            sortedH = sorted(h.items(), key=operator.itemgetter(1))  # sorts H and pciks first item

            x = next(iter(sortedH[0]))  # assumed this posotion has best heuristics
            p.append(x)

            if x == goal:
                return p

            else:
                start = x
    def CarGBFS(graph, start, goal):
        p = []  # host the path
        p.append(start)

        while True:  # creating an infinite loop
            neighbour = graph[start]
            h = {}

            for i in neighbour.difference(p):  # go to all neighbours except those we have visited
                h[i] = Agent.carH(i, goal)  # needs this info to calculate heuristics

            sortedH = sorted(h.items(), key=operator.itemgetter(1))  # sorts H and pciks first item

            x = next(iter(sortedH[0]))  # assumed this posotion has best heuristics
            p.append(x)

            if x == goal:
                return p

            else:
                start = x
    def getCost(pathtoCost,cost):
        pathCost = 0
        i = 0
        while i < len(pathtoCost) - 1:
            l = []
            l.append(pathtoCost[i])
            l.append(pathtoCost[i + 1])
            pathCost = pathCost + int(cost[str(l)])  # Read the cost between the nodes
            i += 1
        return pathCost

    def aStar(graph, start, goal):
        p = []  # hosts path
        p.append(start)

        # infinite loop
        while True:
            # what is next to start position:
            neighbour = graph[start]  # graph contains neighbour of any node
            h = {}
            for i in neighbour.difference(p):  # go to all neighbours escept those visisted.
                l = []
                l.append(str(start))
                l.append(str(i))  # neighbour
                h[i] = Agent.getH(i, goal) + Agent.getCost(l, mappy.WalkCost)  # calc huristics

            # best huristic from list, then pick first item:
            sortedH = sorted(h.items(), key=operator.itemgetter(1))
            x = next(iter(sortedH[0]))  # contains the best huristics
            p.append(x)

            if x == goal:
                return p
            else:
                start = x

    def CaraStar(graph, start, goal):
        p = []  # hosts path
        p.append(start)

        # infinite loop
        while True:
            # what is next to start position:
            neighbour = graph[start]  # graph contains neighbour of any node
            h = {}
            for i in neighbour.difference(p):  # go to all neighbours escept those visisted.
                l = []
                l.append(str(start))
                l.append(str(i))  # neighbour
                h[i] = Agent.getH(i, goal) + Agent.getCost(l, mappy.DriveCost)# calc huristics

            # best huristic from list, then pick first item:
            sortedH = sorted(h.items(), key=operator.itemgetter(1))
            x = next(iter(sortedH[0]))  # contains the best huristics
            p.append(x)

            if x == goal:
                return p
            else:
                start = x

    def Dest2(graph, start, g1, g2):
        y = Agent.Astar(graph, start, g1)
        z = Agent.Astar(graph, g1, g2)

        print(y)
        print(z)
        return y,"     final destination    ",z

    def multidestination():
        if (clicked.get() == clicked2.get() or clicked.get() == clicked3.get()):
            label4.config(text="Please do not enter the same location in both fields. ")
        else:
            label4.config(text="Follow this route to get to your destination: " + str(
            Agent.multiDest(Environment.myGraph, clicked.get(), clicked2.get(), clicked3.get())))

        def third():
            clicked3.set("Gate_A")
            drop3 = OptionMenu(root, clicked3, *location)
            drop3.pack()
            button.pack_forget()
            button5 = Button(root, text="Get Walking Directions", command= Dest2)
            button5.pack(pady =5)

            button = Button(root, text="Get Driving Directions!", command=show)
            button.pack(pady=5)
            button4 = Button(root, text="Additional Destination", command=third)
            button4.pack(pady=5)
            label4 = Label(root, text=" \n")
            label4.pack()
            Button(root, text="EXIT", command=root.destroy).pack()
            root.mainloop()
        return

    def __init__(self, mappy):
        # Change the label text
        def show():
            label.config(text=str((Agent.aStar(mappy.Walk, clicked.get(), clicked1.get()))), pady = 20)

        def showy():
            label.config(text=str((Agent.CaraStar(mappy.Drive, clicked.get(), clicked1.get()))), pady = 20)

        # Dropdown menu options
        options = [
            "Gate A",
            "Administration Block",
            "Administration Parking",
            "Main Lab",
            "Procurement",
            "Mama Africa",
            "Wooden Blocks",
            "Lillian K Beam",
            "Cafeteria",
            "Cafeteria Outdoors Sitting Area",
            "Old Humanities",
            "School of Business",
            "Hostels",
            "Hostels Cafe Latta & Cyber Cafe",
            "Transport Office",
            "Cafe Latta",
            "Cafe Latta Parking Lot",
            "Basketball Court",
            "Auditorium",
            "Auditorium Parking",
            "Bus Parking Lot",
            "Faculty Housing",
            "Library",
            "Library Parking",
            "Student Centre Parking Lot",
            "Student Centre",
            "School of Science",
            "School of Science Parking",
            "Swimming Pool Parking",
            "Swimming Pool",
            "New Humanities",
            "School of Humanities Parking Lot",
            "Gate B",
            "Football Pitch",
            "Rugby Field"
        ]

        # initial menu text
        clicked.set("Gate A")
        clicked1.set("Gate A")
        # Create Dropdown menu
        drop = OptionMenu(root, clicked, *options)
        drop.pack()
        drop2 = OptionMenu(root, clicked1, *options)
        drop2.pack()

        # Create button, it will change label text
        button = Button(root, text="Get Walking Directions! ", padx = 10, pady = 5, command=show).pack()
        button2 = Button(root, text="Get Driving Directions! ", padx = 10, pady = 5, command=showy).pack()
        # Create Label
        label = Label(root, text=" ")
        label.pack()

        # Execute tkinter
        root.mainloop()


theMap = mappy()
theAgent = Agent(theMap)