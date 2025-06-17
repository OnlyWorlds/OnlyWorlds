using System;
using System.Collections.Generic;
[System.Serializable]
public class Character : BaseElement
{
    // Constitution
    public string Physicality;
    public string Mentality;
    public int? Height;
    public int? Weight;
    public List<string> SpeciesIds; = new List<string>();
    public List<string> TraitsIds; = new List<string>();
    public List<string> AbilitiesIds; = new List<string>();
    // Origins
    public string Background;
    public string Motivations;
    public int? BirthDate;
    public string BirthplaceId;
    public List<string> LanguagesIds; = new List<string>();
    // World
    public string Reputation;
    public string LocationId;
    public List<string> ObjectsIds; = new List<string>();
    public List<string> InstitutionsIds; = new List<string>();
    // Personality
    public int? Charisma;
    public int? Coercion;
    public int? Competence;
    public int? Compassion;
    public int? Creativity;
    public int? Courage;
    // Social
    public List<string> FamilyIds; = new List<string>();
    public List<string> FriendsIds; = new List<string>();
    public List<string> RivalsIds; = new List<string>();
    // TTRPG
    public int? Level;
    public int? HitPoints;
    public int? STR;
    public int? DEX;
    public int? CON;
    public int? INT;
    public int? WIS;
    public int? CHA;
}
