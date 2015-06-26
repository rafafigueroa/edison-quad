% Rigid Body Dynamics
% For Handbook of UAV

% Rotation ZXY

syms roll pitch yaw droll dpitch dyaw real
syms m g T real positive


R_AB = [cos(yaw)*cos(pitch)-sin(roll)*sin(yaw)*sin(pitch), ...
        -cos(roll)*sin(yaw), ...
        cos(yaw)*sin(pitch)+cos(pitch)*sin(roll)*sin(yaw);
        cos(pitch)*sin(yaw)+cos(yaw)*sin(roll)*sin(pitch), ...
        cos(roll)*cos(yaw), ...
        sin(yaw)*sin(pitch)-cos(yaw)*cos(pitch)*sin(roll);
        -cos(roll)*sin(pitch), ...
        sin(roll), ...
        cos(roll)*cos(pitch)]
    
ddX = -[0;0;g] + R_AB*[0;0;T/m]

R_pp = [cos(pitch),0,-cos(roll)*sin(pitch);
        0,1,sin(roll);
        sin(pitch),0,cos(roll)*cos(pitch)]
    
inv_R_pp = simplify(inv(R_pp))

syms Ixx Iyy Izz real positive
syms nx ny nz real

I = diag([Ixx, Iyy, Izz])

dn_last = simplify(inv(I)*cross([nx;ny;nz], I*[nx;ny;nz]))

