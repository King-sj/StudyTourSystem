export class User {
  public email:string;
  public password:string;
  public expiration:number;
  public token:string;
  public constructor(email:string = "", password:string="", token:string="",expiration:number=0) {
    this.email = email;
    this.password = password;
    this.expiration = expiration;
    this.token = token;
  }
}