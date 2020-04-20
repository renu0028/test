import junit.framework.TestCase;
public class CalculatorTest extends TestCase{
Calculator cal=new Calculator();
public CalculatorTest(String name){
super(name);
}
public void testSum(){
assertEquals(2,cal.sum(1,1));
assertEquals(20,cal.sum(10,10));
assertEquals(50,cal.sum(40,10));
assertEquals(50,cal.sum(25,25));
assertEquals(0,cal.sum(1,-1));
}}
