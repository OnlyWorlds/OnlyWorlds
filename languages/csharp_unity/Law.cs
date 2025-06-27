using System;
using System.Collections.Generic;
[System.Serializable]
public class Law : BaseElement
{
    // Code
    public string Declaration;
    public string Purpose;
    public int? Date;
    public string ParentLawId;
    public List<string> PenaltiesIds; = new List<string>();
    // World
    public string AuthorId;
    public List<string> LocationsIds; = new List<string>();
    public List<string> ZonesIds; = new List<string>();
    public List<string> ProhibitionsIds; = new List<string>();
    public List<string> AdjudicatorsIds; = new List<string>();
    public List<string> EnforcersIds; = new List<string>();
}
