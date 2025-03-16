class Creature extends BaseModel {
  // Physiology
  final String appearance;
  final int weight;
  final int height;
  final String species; //ms species
  // Lifestyle
  final String behaviour;
  final String demeanour;
  final String traits; //ms trait
  final String abilities; //ms ability
  final String languages; //ms language
  // World
  final int birthDate;
  final String location; //ss location
  final String territory; //ss territory
  // Games
  final String lore;
  final String senses;
  final int hitPoints;
  final int armorClass;
  final int challengeRating;
  final int speed;
  final int ttStr; // maxint
  final int ttInt; // maxint
  final int ttCon; // maxint
  final int ttDex; // maxint
  final int ttWis; // maxint
  final int ttCha; // maxint
  final String actions; //ms ability
  final String reactions; //ms construct
  final String alignment;
}
