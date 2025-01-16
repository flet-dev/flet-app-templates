import 'package:flet/flet.dart';

import '{{cookiecutter.project_name}}.dart';

CreateControlFactory createControl = (CreateControlArgs args) {
  switch (args.control.type) {
    case "{{cookiecutter.project_name}}":
      return {{cookiecutter.control_name}}Control(
        parent: args.parent,
        control: args.control,
      );
    default:
      return null;
  }
};

void ensureInitialized() {
  // nothing to initialize
}
