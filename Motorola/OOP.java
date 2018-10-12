public class Human {
   public double weight = 0;
  
   public double getPower() {
       return this.weight;
   }
  
   public Boolean isEqualToPower(Human h) {
       // 只要是人，都有取得自己威力的 method，叫做 getPower。
       // 但是骨子裡，不同人種 getPower 的方式卻不一定相同。
       // 這就是多型的應用。
      
       return this.getPower() == h.getPower();
   }
}
 
public class Black extends Human {
   public double getPower() {
       return this.weight * 1.5;
   }
  
   public void black_method() {
       // only for black
   }
}
 
public class White extends Human {
   public double getPower() {
       return this.weight * 1.2;
   }
  
   public void white_method() {
       // only for white
   }
}
