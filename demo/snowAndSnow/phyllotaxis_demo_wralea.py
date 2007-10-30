
# This file has been generated at $TIME

from openalea.core import *

def register_packages(pkgmanager):
    
    metainfo = {} 
    if pkgmanager.has_key( "Demo.PhyllotaxisModel" ): pkg = pkgmanager[ "Demo.PhyllotaxisModel" ]
    else: pkg = UserPackage("Demo.PhyllotaxisModel", metainfo)

    


    #nf = CompositeNodeFactory(name=' Snow&Snow model (composed)', 
    #                          description='', 
    #                          category='Demo',
    #                          doc='',
    #                          inputs=[],
    #                          outputs=[],
    #                          elt_factory={2: ('PhyllotaxisModel', 'Snow&Snow phyllotaxis model'), 3: ('PhyllotaxisModel', 'Prim time differences'), 4: ('PhyllotaxisModel', 'Prim absolute angles'), 5: ('System', 'annotation'), 6: ('PhyllotaxisModel', 'Prim time creation'), 7: ('PlotTools', 'VS Plot'), 8: ('PlotTools', 'PointLine Style'), 9: ('PlotTools', 'VS Plot'), 10: ('System', 'rendez vous'), 11: ('PhyllotaxisModel', 'Prim divergence angles'), 26: ('My Package', 'Snow&Snow loop'), 27: ('System', 'annotation'), 28: ('System', 'annotation'), 29: ('System', 'annotation')},
    #                          elt_connections={135572928: (2, 0, 26, 0), 135572880: (2, 0, 11, 0), 135572964: (4, 0, 7, 0), 135573000: (2, 0, 6, 0), 135572892: (9, 0, 10, 1), 135572940: (6, 0, 7, 0), 135572784: (26, 0, 2, 1), 135572976: (8, 0, 7, 0), 135572904: (7, 0, 10, 0), 135573012: (2, 0, 4, 0), 135572952: (2, 0, 3, 0), 135572868: (11, 0, 9, 0), 135572988: (3, 0, 8, 0), 135572856: (11, 0, 7, 0)},
    #                          elt_data={2: {'lazy': True, 'hide': False, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'Snow&Snow phyllotaxis model', 'posx': 58.090948223503744, 'posy': -663.50797413420332, 'minimal': False}, 3: {'lazy': True, 'hide': False, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'Prim time differences', 'posx': -258.78175222115715, 'posy': -504.86740662308677, 'minimal': False}, 4: {'lazy': True, 'hide': False, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'Prim absolute angles', 'posx': 214.96824777884291, 'posy': -502.36740662308677, 'minimal': False}, 5: {'txt': 'Model layer', 'posx': -477.5616765717723, 'posy': -657.15752075260991}, 6: {'lazy': True, 'hide': False, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'Prim time creation', 'posx': 1.2182477788429082, 'posy': -504.86740662308677, 'minimal': False}, 7: {'lazy': True, 'hide': False, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'VS Plot', 'posx': -83.781752221157092, 'posy': -241.11740662308671, 'minimal': False}, 8: {'lazy': True, 'hide': False, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'PointLine Style', 'posx': -242.53175222115715, 'posy': -363.61740662308671, 'minimal': False}, 9: {'lazy': True, 'hide': False, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'VS Plot', 'posx': 269.06650795609147, 'posy': -241.54262410093054, 'minimal': False}, 10: {'lazy': True, 'hide': False, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'rendez vous', 'posx': 88.237820784796611, 'posy': -153.14739202674389, 'minimal': False}, 11: {'lazy': True, 'hide': False, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'Prim divergence angles', 'posx': 450.09000219793694, 'posy': -499.69044268779004, 'minimal': False}, 27: {'txt': 'Model inspectors', 'posx': -489.80684776592034, 'posy': -506.133742691451}, '__out__': {'lazy': True, 'hide': False, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'Out', 'posx': 20.0, 'posy': 250.0, 'minimal': False}, 26: {'lazy': True, 'hide': False, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'Snow&Snow loop', 'posx': -193.32088090873697, 'posy': -672.18911802212233, 'minimal': False}, '__in__': {'lazy': True, 'hide': False, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'In', 'posx': 20.0, 'posy': 5.0, 'minimal': False}, 28: {'txt': 'Plot modificators', 'posx': -481.64340030315503, 'posy': -363.27341209305757}, 29: {'txt': 'Plots', 'posx': -475.52081470608096, 'posy': -234.6991145545035}},
    #                          elt_value={2: [(0, '1.1000000000000001'), (2, '20'), (3, 'True'), (4, 'True'), (5, 'True')], 3: [], 4: [], 5: [], 6: [], 7: [(1, "'PointLine'"), (2, "'Phyllotaxis summary'"), (3, "'Primordia'"), (4, "'Time/Angle'"), (5, '0')], 8: [(1, "'Default'"), (2, "'Default'"), (3, "'Default'"), (4, "'b'")], 9: [(1, "'Hist'"), (2, "'Divergence angle Hisogram'"), (3, "'Primordium'"), (4, "'Angle'"), (5, '1')], 10: [], 11: [], 27: [], '__out__': [], 26: [], '__in__': [], 28: [], 29: []},
    #                          lazy=True,
    #                          )
    #
    #pkg.add_factory(nf)


    nf = CompositeNodeFactory(name=' Snow&Snow model (decomposed)', 
                              description='', 
                              category='Demo',
                              doc='',
                              inputs=[],
                              outputs=[],
                              elt_factory={2: ('PhyllotaxisModel', 'Snow&Snow phyllotaxis model'), 3: ('PhyllotaxisModel', 'Prim time differences'), 4: ('PhyllotaxisModel', 'Prim absolute angles'), 5: ('System', 'annotation'), 6: ('PhyllotaxisModel', 'Prim time creation'), 7: ('PlotTools', 'VS Plot'), 8: ('PlotTools', 'PointLine Style'), 9: ('PlotTools', 'VS Plot'), 10: ('System', 'rendez vous'), 11: ('PhyllotaxisModel', 'Prim divergence angles'), 12: ('Catalog.Python', 'getitem'), 13: ('Catalog.Data', 'string'), 14: ('Catalog.Data', 'int'), 15: ('Catalog.Math', '+'), 16: ('Catalog.Python', 'range'), 17: ('System', 'iter'), 18: ('Catalog.Python', 'ifelse'), 19: ('Catalog.Data', 'int'), 20: ('Catalog.Data', 'int'), 21: ('System', 'annotation'), 22: ('System', 'annotation'), 23: ('System', 'annotation'), 24: ('System', 'annotation'), 25: ('System', 'annotation'), 26: ('System', 'annotation'), 27: ('System', 'annotation'), 28: ('System', 'annotation'), 29: ('System', 'annotation')},
                              elt_connections={135572736: (12, 0, 18, 0), 135572868: (11, 0, 9, 0), 135573000: (2, 0, 6, 0), 135572748: (13, 0, 12, 1), 135572880: (2, 0, 11, 0), 135573012: (2, 0, 4, 0), 135572760: (18, 0, 16, 0), 135572892: (9, 0, 10, 1), 135572772: (18, 0, 15, 0), 135572904: (7, 0, 10, 0), 135572784: (19, 0, 18, 2), 135572916: (2, 0, 12, 0), 135572796: (20, 0, 16, 2), 135572928: (17, 0, 2, 1), 135572808: (12, 0, 18, 1), 135572940: (6, 0, 7, 0), 135572820: (14, 0, 15, 1), 135572952: (2, 0, 3, 0), 135572832: (16, 0, 17, 0), 135572964: (4, 0, 7, 0), 135572844: (15, 0, 16, 1), 135572976: (8, 0, 7, 0), 135572856: (11, 0, 7, 0), 135572988: (3, 0, 8, 0)},
                              elt_data={2: {'lazy': True, 'hide': False, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'Snow&Snow phyllotaxis model', 'posx': 58.090948223503744, 'posy': -663.50797413420332, 'minimal': False}, 3: {'lazy': True, 'hide': False, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'Prim time differences', 'posx': -258.78175222115715, 'posy': -504.86740662308677, 'minimal': False}, 4: {'lazy': True, 'hide': False, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'Prim absolute angles', 'posx': 214.96824777884291, 'posy': -502.36740662308677, 'minimal': False}, 5: {'txt': 'Model layer', 'posx': -477.5616765717723, 'posy': -657.15752075260991}, 6: {'lazy': True, 'hide': False, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'Prim time creation', 'posx': 1.2182477788429082, 'posy': -504.86740662308677, 'minimal': False}, 7: {'lazy': True, 'hide': False, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'VS Plot', 'posx': -83.781752221157092, 'posy': -241.11740662308671, 'minimal': False}, 8: {'lazy': True, 'hide': False, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'PointLine Style', 'posx': -242.53175222115715, 'posy': -363.61740662308671, 'minimal': False}, 9: {'lazy': True, 'hide': False, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'VS Plot', 'posx': 269.06650795609147, 'posy': -241.54262410093054, 'minimal': False}, 10: {'lazy': True, 'hide': False, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'rendez vous', 'posx': 88.237820784796611, 'posy': -153.14739202674389, 'minimal': False}, 11: {'lazy': True, 'hide': False, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'Prim divergence angles', 'posx': 450.09000219793694, 'posy': -499.69044268779004, 'minimal': False}, 12: {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'getitem', 'posx': 811.21228031058467, 'posy': -629.63003091635483, 'minimal': False}, 13: {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': "'current_prim'", 'posx': 837.46228031058467, 'posy': -687.13003091635483, 'minimal': False}, 14: {'lazy': True, 'hide': False, 'port_hide_changed': set([]), 'priority': 0, 'caption': '20', 'posx': 1556.2122803105847, 'posy': -420.88003091635488, 'minimal': False}, 15: {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': '+', 'posx': 903.71228031058467, 'posy': -297.13003091635483, 'minimal': False}, 16: {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'range', 'posx': 878.71228031058467, 'posy': -237.13003091635483, 'minimal': False}, 17: {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'iter', 'posx': 889.96228031058467, 'posy': -190.88003091635483, 'minimal': False}, 18: {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'ifelse', 'posx': 808.71228031058467, 'posy': -417.13003091635488, 'minimal': False}, 19: {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': '0', 'posx': 854.96228031058467, 'posy': -465.88003091635494, 'minimal': False}, 20: {'lazy': True, 'hide': False, 'port_hide_changed': set([]), 'priority': 0, 'caption': '1', 'posx': 1556.2122803105847, 'posy': -335.88003091635483, 'minimal': False}, 21: {'txt': 'Number of generated primordia', 'posx': 1181.2122803105847, 'posy': -417.13003091635488}, 22: {'txt': 'Plots refresh rate', 'posx': 1342.4622803105847, 'posy': -330.88003091635483}, 23: {'txt': 'Getting the model\nresults, selecting the\ncorrect one', 'posx': 989.96228031058467, 'posy': -689.63003091635483}, 24: {'txt': 'Solving the problem \nof None entry', 'posx': 896.21228031058467, 'posy': -455.88003091635494}, 25: {'txt': 'Calculating current\nstep number and \npropagating it with\niterator', 'posx': 956.21228031058467, 'posy': -248.38003091635483}, 26: {'txt': 'PARAMETERS:', 'posx': 1321.2122803105847, 'posy': -472.13003091635488}, 27: {'txt': 'Model inspectors', 'posx': -489.80684776592034, 'posy': -506.133742691451}, 28: {'txt': 'Plot modificators', 'posx': -481.64340030315503, 'posy': -363.27341209305757}, 29: {'txt': 'Plots', 'posx': -475.52081470608096, 'posy': -234.6991145545035}, '__out__': {'lazy': True, 'hide': False, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'Out', 'posx': 20.0, 'posy': 250.0, 'minimal': False}, '__in__': {'lazy': True, 'hide': False, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'In', 'posx': 20.0, 'posy': 5.0, 'minimal': False}},
                              elt_value={2: [(0, '1.1000000000000001'), (2, '20'), (3, 'True'), (4, 'True'), (5, 'True')], 3: [], 4: [], 5: [], 6: [], 7: [(1, "'PointLine'"), (2, "'Phyllotaxis summary'"), (3, "'Primordia'"), (4, "'Time/Angle'"), (5, '0')], 8: [(1, "'Default'"), (2, "'Default'"), (3, "'Default'"), (4, "'b'")], 9: [(1, "'Hist'"), (2, "'Divergence angle Hisogram'"), (3, "'Primordium'"), (4, "'Angle'"), (5, '1')], 10: [], 11: [], 12: [], 13: [(0, "'current_prim'")], 14: [(0, '20')], 15: [], 16: [], 17: [], 18: [], 19: [(0, '0')], 20: [(0, '1')], 21: [], 22: [], 23: [], 24: [], 25: [], 26: [], 27: [], 28: [], 29: [], '__out__': [], '__in__': []},
                              lazy=True,
                              )

    pkg.add_factory(nf)
    #
    #
    #
    #nf = CompositeNodeFactory(name=' Snow&Snow loop', 
    #                          description='This element is used to iterate the S&S model.', 
    #                          category='Demo',
    #                          doc='',
    #                          inputs=[{'interface': IDict, 'name': 'IN1'}],
    #                          outputs=[{'interface': IInt, 'name': 'OUT1'}],
    #                          elt_factory={2: ('Catalog.Python', 'getitem'), 3: ('Catalog.Data', 'string'), 4: ('Catalog.Data', 'int'), 5: ('Catalog.Math', '+'), 6: ('Catalog.Python', 'range'), 7: ('System', 'iter'), 8: ('Catalog.Python', 'ifelse'), 9: ('Catalog.Data', 'int'), 10: ('Catalog.Data', 'int'), 11: ('System', 'annotation'), 12: ('System', 'annotation'), 13: ('System', 'annotation'), 14: ('System', 'annotation'), 15: ('System', 'annotation'), 16: ('System', 'annotation')},
    #                          elt_connections={135572928: (5, 0, 6, 1), 135572880: (10, 0, 6, 2), 135572964: (7, 0, '__out__', 0), 135573000: (6, 0, 7, 0), 135572892: (4, 0, 5, 1), 135572940: (2, 0, 8, 1), 135572976: ('__in__', 0, 2, 0), 135572904: (9, 0, 8, 2), 135573012: (8, 0, 5, 0), 135572952: (8, 0, 6, 0), 135572916: (3, 0, 2, 1), 135572988: (2, 0, 8, 0)},
    #                          elt_data={2: {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'getitem', 'posx': 93.75, 'posy': 106.25, 'minimal': False}, 3: {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': "'current_prim'", 'posx': 120.0, 'posy': 48.75, 'minimal': False}, 4: {'lazy': True, 'hide': False, 'port_hide_changed': set([]), 'priority': 0, 'caption': '20', 'posx': 838.75, 'posy': 315.0, 'minimal': False}, 5: {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': '+', 'posx': 186.25, 'posy': 438.75, 'minimal': False}, 6: {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'range', 'posx': 161.25, 'posy': 498.75, 'minimal': False}, 7: {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'iter', 'posx': 172.5, 'posy': 545.0, 'minimal': False}, 8: {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'ifelse', 'posx': 91.25, 'posy': 318.75, 'minimal': False}, 9: {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': '0', 'posx': 137.5, 'posy': 270.0, 'minimal': False}, 10: {'lazy': True, 'hide': False, 'port_hide_changed': set([]), 'priority': 0, 'caption': '1', 'posx': 838.75, 'posy': 400.0, 'minimal': False}, 11: {'txt': 'Number of generated primordia', 'posx': 463.75, 'posy': 318.75}, 12: {'txt': 'Plots refresh rate', 'posx': 625.0, 'posy': 405.0}, 13: {'txt': 'Getting the model\nresults, selecting the\ncorrect one', 'posx': 272.5, 'posy': 46.25}, 14: {'txt': 'Solving the problem \nof None entry', 'posx': 178.75, 'posy': 280.0}, 15: {'txt': 'Calculating current\nstep number and \npropagating it with\niterator', 'posx': 238.75, 'posy': 487.5}, 16: {'txt': 'PARAMETERS:', 'posx': 603.75, 'posy': 263.75}, '__out__': {'lazy': True, 'hide': False, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'Out', 'posx': 28.75, 'posy': 617.5, 'minimal': False}, '__in__': {'lazy': True, 'hide': True, 'port_hide_changed': set([]), 'priority': 0, 'caption': 'In', 'posx': 20.0, 'posy': 5.0, 'minimal': False}},
    #                          elt_value={2: [], 3: [(0, "'current_prim'")], 4: [(0, '20')], 5: [], 6: [], 7: [], 8: [], 9: [(0, '0')], 10: [(0, '1')], 11: [], 12: [], 13: [], 14: [], 15: [], 16: [], '__out__': [], '__in__': []},
    #                          lazy=True,
    #                          )
    #
    #pkg.add_factory(nf)


    pkgmanager.add_package(pkg)


