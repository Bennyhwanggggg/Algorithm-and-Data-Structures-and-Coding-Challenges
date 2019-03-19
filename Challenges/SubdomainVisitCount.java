class Solution {
    public List<String> subdomainVisits(String[] cpdomains) {
        Map<String, Integer> freq = new HashMap<>();
        for(String cpd: cpdomains){
            String[] countAndDomain = cpd.split(" ");
            int count = Integer.parseInt(countAndDomain[0]);
            String domain = countAndDomain[1];
            int start = 0;
            while(true){
                freq.put(domain, freq.getOrDefault(domain, 0)+count);
                start = domain.indexOf('.');
                if(start < 0){
                    break;
                }
                domain = domain.substring(start+1);
            }
        }
        List<String> res = new ArrayList<>();
        for(Map.Entry<String, Integer> e: freq.entrySet()){
            res.add(e.getValue() + " " + e.getKey());
        }
        return res;
    }
}