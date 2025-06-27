class Location extends BaseElement {
  // Setting
  final String form;
  final String function;
  final int foundingDate;
  final String parentLocation; //ss location
  final String populations; //ms collective
  // Politics
  final String politicalClimate;
  final String primaryPower; //ss institution
  final String governingTitle; //ss title
  final String secondaryPowers; //ms institution
  final String zone; //ss zone
  final String rival; //ss location
  final String partner; //ss location
  // World
  final String customs;
  final String founders; //ms character
  final String cults; //ms construct
  final String delicacies; //ms species
  // Production
  final String extractionMethods; //ms construct
  final String extractionGoods; //ms construct
  final String industryMethods; //ms construct
  final String industryGoods; //ms construct
  // Commerce
  final String infrastructure;
  final String extractionMarkets; //ms location
  final String industryMarkets; //ms location
  final String currencies; //ms construct
  // Construction
  final String architecture;
  final String buildings; //ms object
  final String buildingMethods; //ms construct
  // Defense
  final String defensibility;
  final int elevation;
  final String fighters; //ms construct
  final String defensiveObjects; //ms object
}
