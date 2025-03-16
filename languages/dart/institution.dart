class Institution extends BaseModel {
  // Foundation
  final String premise;
  final int foundDate;
  final int endDate;
  final String parentInstitution; //ss institution
  // Claim
  final String territories; //ms territory
  final String objects; //ms object
  final String creatures; //ms creature
  final String legal; //ms law
  // World
  final String situation;
  final String cooperates; //ms institution
  final String competition; //ms institution
  final String constructs; //ms construct
  final String phenomena; //ms phenomenon
}
