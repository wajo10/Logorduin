
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'Azar Borrapantalla Cuenta Division EQUALS Elegir Elemento FLOAT INT Inic LeftSquareBracket Menos NAME Potencia Pri Producto RC Resto RightSquareBracket Sen Space Suma Ultimo Var\n    statement : Var Space NAME Space EQUALS Space expression\n    statement : Inic Space NAME Space EQUALS Space expression\n                 | Inic Space NAME Space EQUALS Space function\n                 \n    statement : Var Space NAME\n    \n    statement : expression\n    expression : INT\n                  | FLOAT\n                  | function\n    expression : NAME\n    operaciones : expression Space expression\n                | expression Space operaciones\n                function : Suma Space operaciones\n                function : Azar Space expressionfunction : Producto Space operaciones\n                function :  Potencia Space expression Space expressionfunction :  Division Space expression Space expressionfunction :  Resto Space expression Space expressionfunction :  RC Space expressionfunction :  Sen Space expressionfunction : Elegir Space LeftSquareBracket operaciones RightSquareBracketfunction :  Borrapantalla'
    
_lr_action_items = {'Var':([0,],[2,]),'Inic':([0,],[5,]),'INT':([0,21,22,23,24,25,26,27,28,41,44,45,46,47,57,58,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'FLOAT':([0,21,22,23,24,25,26,27,28,41,44,45,46,47,57,58,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'NAME':([0,19,20,21,22,23,24,25,26,27,28,41,44,45,46,47,57,58,],[3,30,31,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,]),'Suma':([0,21,22,23,24,25,26,27,28,41,44,45,46,47,57,58,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'Azar':([0,21,22,23,24,25,26,27,28,41,44,45,46,47,57,58,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'Producto':([0,21,22,23,24,25,26,27,28,41,44,45,46,47,57,58,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'Potencia':([0,21,22,23,24,25,26,27,28,41,44,45,46,47,57,58,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'Division':([0,21,22,23,24,25,26,27,28,41,44,45,46,47,57,58,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'Resto':([0,21,22,23,24,25,26,27,28,41,44,45,46,47,57,58,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'RC':([0,21,22,23,24,25,26,27,28,41,44,45,46,47,57,58,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'Sen':([0,21,22,23,24,25,26,27,28,41,44,45,46,47,57,58,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'Elegir':([0,21,22,23,24,25,26,27,28,41,44,45,46,47,57,58,],[17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'Borrapantalla':([0,21,22,23,24,25,26,27,28,41,44,45,46,47,57,58,],[18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'$end':([1,3,4,6,7,8,18,30,32,34,35,39,40,51,52,53,54,55,56,59,60,61,],[0,-9,-5,-8,-6,-7,-21,-4,-12,-13,-14,-18,-19,-10,-11,-15,-16,-17,-20,-1,-2,-3,]),'Space':([2,3,5,6,7,8,9,10,11,12,13,14,15,16,17,18,30,31,32,33,34,35,36,37,38,39,40,49,50,51,52,53,54,55,56,],[19,-9,20,-8,-6,-7,21,22,23,24,25,26,27,28,29,-21,42,43,-12,44,-13,-14,45,46,47,-18,-19,57,58,44,-11,-15,-16,-17,-20,]),'RightSquareBracket':([3,6,7,8,18,32,34,35,39,40,48,51,52,53,54,55,56,],[-9,-8,-6,-7,-21,-12,-13,-14,-18,-19,56,-10,-11,-15,-16,-17,-20,]),'LeftSquareBracket':([29,],[41,]),'EQUALS':([42,43,],[49,50,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'expression':([0,21,22,23,24,25,26,27,28,41,44,45,46,47,57,58,],[4,33,34,33,36,37,38,39,40,33,51,53,54,55,59,60,]),'function':([0,21,22,23,24,25,26,27,28,41,44,45,46,47,57,58,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,61,]),'operaciones':([21,23,41,44,],[32,35,48,52,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> Var Space NAME Space EQUALS Space expression','statement',7,'p_statement_create','compYacc.py',12),
  ('statement -> Inic Space NAME Space EQUALS Space expression','statement',7,'p_statement_assign','compYacc.py',20),
  ('statement -> Inic Space NAME Space EQUALS Space function','statement',7,'p_statement_assign','compYacc.py',21),
  ('statement -> Var Space NAME','statement',3,'p_statement_create_empty','compYacc.py',32),
  ('statement -> expression','statement',1,'p_statement_expr','compYacc.py',41),
  ('expression -> INT','expression',1,'p_expression_Number','compYacc.py',48),
  ('expression -> FLOAT','expression',1,'p_expression_Number','compYacc.py',49),
  ('expression -> function','expression',1,'p_expression_Number','compYacc.py',50),
  ('expression -> NAME','expression',1,'p_expression_name','compYacc.py',56),
  ('operaciones -> expression Space expression','operaciones',3,'p_operaciones','compYacc.py',66),
  ('operaciones -> expression Space operaciones','operaciones',3,'p_operaciones','compYacc.py',67),
  ('function -> Suma Space operaciones','function',3,'p_suma','compYacc.py',81),
  ('function -> Azar Space expression','function',3,'p_Azar','compYacc.py',89),
  ('function -> Producto Space operaciones','function',3,'p_producto','compYacc.py',109),
  ('function -> Potencia Space expression Space expression','function',5,'p_Menos','compYacc.py',115),
  ('function -> Division Space expression Space expression','function',5,'p_Division','compYacc.py',120),
  ('function -> Resto Space expression Space expression','function',5,'p_Resto','compYacc.py',126),
  ('function -> RC Space expression','function',3,'p_RC','compYacc.py',131),
  ('function -> Sen Space expression','function',3,'p_Sen','compYacc.py',136),
  ('function -> Elegir Space LeftSquareBracket operaciones RightSquareBracket','function',5,'p_Elegir','compYacc.py',148),
  ('function -> Borrapantalla','function',1,'p_Borrapantalla','compYacc.py',154),
]
