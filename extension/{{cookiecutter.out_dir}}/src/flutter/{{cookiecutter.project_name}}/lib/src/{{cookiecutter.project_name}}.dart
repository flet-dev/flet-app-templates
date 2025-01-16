import 'package:flet/flet.dart';
import 'package:flutter/material.dart';

class {{cookiecutter.control_name}}Control extends StatelessWidget {
  final Control? parent;
  final Control control;

  const {{cookiecutter.control_name}}Control({
    super.key,
    required this.parent,
    required this.control,
  });

  @override
  Widget build(BuildContext context) {
    var color = control.attrColor("color", context);
    String text = control.attrString("value", "")!;
    Widget myControl = Text(text, style: TextStyle(color: color),);


    return constrainedControl(context, myControl, parent, control);
  }
}
