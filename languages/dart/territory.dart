class Territory extends BaseElement {
  // Situation
  final String terrain;
  final int size;
  final String parentTerritory; //ss territory
  // Yield
  final String maintenance;
  final int primaryOutput;
  final int secondaryOutput;
  final String primaryResource; //ss construct
  final String secondaryResources; //ms construct
  // World
  final String history;
  final String occupants; //ms species
  final String occurrences; //ms phenomenon
}
