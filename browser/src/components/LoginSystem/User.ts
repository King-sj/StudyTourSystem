export class User {
  public email:string;
  public password:string;
  public expiration:number;
  public constructor(email:string = "", password:string="", expiration:number=0) {
    this.email = email;
    this.password = password;
    this.expiration = expiration;
  }
}