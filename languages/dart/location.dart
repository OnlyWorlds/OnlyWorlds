class Location extends BaseModel {
  // Locality
  final String scene;
  final String activity;
  final int foundingDate;
  final int populationSize;
  final String parentLocation; //ss location
  final String populations; //ms collective
  // Culture
  final String traditions;
  final String celebrations;
  final String primaryCult; //ss construct
  final String secondaryCults; //ms construct
  final String delicacies; //ms species
  // World
  final String coordinates;
  final String founders; //ms character
  // Construction
  final String logistics;
  final String architecture;
  final int constructionRate; // maxint
  final String buildings; //ms location
  final String buildingExpertise; //ms construct
  // Production
  final String extraction;
  final String industry;
  final int extractionOutput;
  final int industryOutput;
  final String primaryResource; //ss construct
  final String primaryIndustry; //ss construct
  final String secondaryResources; //ms construct
  final String secondaryIndustries; //ms construct
  // Commerce
  final String trade;
  final String infrastructure;
  final String currency;
  final String primaryExtractionMarket; //ss location
  final String primaryIndustryMarket; //ss location
  final String secondaryExtractionMarkets; //ms location
  final String secondaryIndustryMarkets; //ms location
  // Localpolitics
  final String government;
  final String opposition;
  final String governingTitle; //ss title
  final String primaryFaction; //ss institution
  final String secondaryFactions; //ms institution
  // Regionalpolitics
  final String territorialPolicies;
  final String territory; //ss territory
  final String rival; //ss location
  final String friend; //ss location
  final String softInfluenceOn; //ms location
  final String hardInfluenceOn; //ms location
  // Strategics
  final String defensibility;
  final int height;
  final String primaryFighter; //ss institution
  final String secondaryFighters; //ms institution
  final String defenses; //ms location
  final String fortifications; //ms object
}
