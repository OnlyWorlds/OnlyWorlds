using System;
using System.Collections.Generic;
[System.Serializable]
public class Ability : BaseElement
{
    // Mechanics
    public string Activation;
    public int? Duration;
    public int? Potency;
    public int? Range;
    public List<string> EffectsIds; = new List<string>();
    // Enablement
    public string Challenges;
    public string SourceId;
    public List<string> TalentsIds; = new List<string>();
    public List<string> InstrumentsIds; = new List<string>();
    public List<string> RequisitesIds; = new List<string>();
    // World
    public string Prevalence;
    public string TraditionId;
    public string LocusId;
}
