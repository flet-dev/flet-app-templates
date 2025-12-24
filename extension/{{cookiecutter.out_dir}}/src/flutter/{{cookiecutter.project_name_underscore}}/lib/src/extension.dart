import 'package:flet/flet.dart';

import '{{cookiecutter.project_name_underscore}}.dart';

class Extension extends FletExtension {
  @override
  Widget? createWidget(Key? key, Control control) {
    switch (control.type) {
      case "{{cookiecutter.project_name_underscore}}":
        return {{cookiecutter.control_name}}Control(control: control);
      default:
        return null;
    }
  }
}
